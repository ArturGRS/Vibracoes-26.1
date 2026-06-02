# coding: utf-8
'''
Módulo para Análise de Sinais de Vibração/Aceleração.
Dividio por experimento, permite a analise dos dados, plotagem de fft,
identificação de modos fundamentais.
'''

from os import path
import pandas as pd
import numpy as np
import librosa as lb
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, detrend, butter, filtfilt, coherence
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class Experimento:
    
    def __init__(self, titulo: str, 
                arquivo_acelerometro: str, 
                arquivo_giroscopio: str, 
                taxa_amostragem: int) -> None:
        
        self.acel = Path(arquivo_acelerometro)
        self.giro = Path(arquivo_giroscopio)
        self.taxa_amostragem = taxa_amostragem
        self.titulo = titulo

        self.acel_sinais: Dict[str, np.ndarray] = {}
        self.giro_sinais: Dict[str, np.ndarray] = {}

        self._acel_mapa_colunas = {
            "x": "Acceleration x (m/s^2)",
            "y": "Acceleration y (m/s^2)",
            "z": "Acceleration z (m/s^2)"
        }
        self._giro_mapa_colunas = {
            "x":"Gyroscope x (rad/s)",
            "y":"Gyroscope y (rad/s)",
            "z":"Gyroscope z (rad/s)"
        }
        
        self._carregar()

    def __repr__(self) -> str:
        return (f'{'='*40}\nDados de Aceleração: {self.acel}\nDados de Giroscópio: {self.giro}\n{'='*40}'+
                f'\n{self._acel_mapa_colunas = }\n{self._giro_mapa_colunas = }')

    def _carregar(self) -> None:

        try:
            if self.acel.suffix == '.csv':
                df_acel, df_giro = pd.read_csv(self.acel), pd.read_csv(self.giro)
            elif self.acel.suffix == '.xls':
                df_acel, df_giro = pd.read_excel(self.acel), pd.read_excel(self.giro)

        except:
            print('Dá uma olhada na extensão dos arquivos que eles estão erradas')

        a = 60
        print(f'{'='*a}\n {'Acelerometro': ^30}\n{'='*a}')
        for eixo, nome_coluna in self._acel_mapa_colunas.items():

            if nome_coluna in df_acel.columns:
                sinal = df_acel[nome_coluna].dropna().values.astype(np.float64)
                self.acel_sinais[eixo] = sinal
                print(f"  -> Eixo {eixo.lower()} carregado com sucesso ({len(sinal)} amostras).")

        print(f'{'='*a}\n {'Giroscópio': ^30}\n{'='*a}')
        for eixo, nome_coluna in self._giro_mapa_colunas.items():
            
            if nome_coluna in df_giro.columns:
                sinal = df_giro[nome_coluna].dropna().values.astype(np.float64)
                self.giro_sinais[eixo] = sinal
                print(f"  -> Eixo {eixo.lower()} carregado com sucesso ({len(sinal)} amostras).")
        print(f'{'='*a}\n{'='*a}')

    def ver_dados(self, inicio: float = None, 
                fim: float = None, 
                limpar: bool = False, 
                salvar: bool = False) -> None:

        def _limpar_sinais(_sinal) -> np.array:

            _sinal = detrend(_sinal)

            # Normalizando
            max_abs_val = np.max(np.abs(_sinal))
            if max_abs_val > 0:
                sinal_normalizado = _sinal / max_abs_val

            # Retirando as frequências altas e baixas
            nyq = self.taxa_amostragem / 2
            b, a = butter(4, [1/nyq, 50/nyq], btype='band')
            return filtfilt(b, a, sinal_normalizado)
            
        inicio_idx = int(inicio * self.taxa_amostragem) if inicio is not None else 0
        fim_idx = int(fim * self.taxa_amostragem) if fim is not None else None

        figure, axes = plt.subplots(3, 2, figsize=(12, 9), sharey=False)
        figure.suptitle(f"{self.titulo.replace('_',' ').title()}", fontsize=14, fontweight='bold')

        for index, (eixo, sinal) in enumerate(self.acel_sinais.items()):

            sinal = sinal[inicio_idx:fim_idx]

            if limpar:
                sinal = _limpar_sinais(sinal)

            ax = axes[index, 0]
            t = np.arange(len(sinal)) / self.taxa_amostragem
            ax.plot(t, sinal, color="blue", linewidth=0.5)
            ax.set_title(f"Aceleração Eixo {eixo.upper()}", fontsize=11)
            ax.set_xlabel("Tempo (s)")
            ax.set_ylabel("Amplitude (m/s²)")
            ax.grid(True, linestyle='--', alpha=0.5)

        for index, (eixo, sinal) in enumerate(self.giro_sinais.items()):

            sinal = sinal[inicio_idx:fim_idx]

            if limpar:
                sinal = _limpar_sinais(sinal)

            sinal = sinal[200:]
            ax = axes[index, 1]
            t = np.arange(len(sinal)) / self.taxa_amostragem
            ax.plot(t, sinal, color="red", linewidth=0.5)
            ax.set_title(f"Giroscópio Eixo {eixo.upper()}", fontsize=11)
            ax.set_xlabel("Tempo (s)")
            ax.set_ylabel("Amplitude (rad/s)")
            ax.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout(rect=[0, 0, 1, 0.96])

        if salvar:
            plt.savefig(f"resultados/sensores/{self.titulo}.png", dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()

    def ver_frequencias(self, inicio: float = None,
                    fim: float = None,
                    limite_frequencia: float = 25,
                    salvar: bool = False) -> None:

        def _calcular_fft(sinal: np.ndarray):
            n_amostras = len(sinal)

            frequencias = np.fft.rfftfreq(n_amostras, d=1.0 / self.taxa_amostragem)
            espectro = np.abs(np.fft.rfft(sinal))

            limite_ruido = np.max(espectro) * 0.05
            picos_indices, _ = find_peaks(
                espectro,
                height=limite_ruido,
                distance=int(n_amostras / self.taxa_amostragem)
            )

            mascara = frequencias <= limite_frequencia
            frequencias_filtradas = frequencias[mascara]
            espectro_filtrado = espectro[mascara]

            picos_validos = picos_indices[picos_indices < len(frequencias_filtradas)]
            return frequencias_filtradas, espectro_filtrado, frequencias_filtradas[picos_validos], espectro_filtrado[picos_validos]

        inicio_idx = int(inicio * self.taxa_amostragem) if inicio is not None else 0
        fim_idx = int(fim * self.taxa_amostragem) if fim is not None else None

        figure, axes = plt.subplots(3, 2, figsize=(12, 9), sharey=False)
        figure.suptitle(f"{self.titulo.replace('_',' ').title()} — Espectro de Frequências", fontsize=14, fontweight='bold')

        for index, (eixo, sinal) in enumerate(self.acel_sinais.items()):
            sinal = sinal[inicio_idx:fim_idx]
            freqs, espectro, picos_f, picos_a = _calcular_fft(sinal)

            ax = axes[index, 0]
            ax.plot(freqs, espectro, color="blue", linewidth=0.8)
            ax.plot(picos_f, picos_a, "x", color="orange", markersize=8, label="Picos")
            for f, a in zip(picos_f, picos_a):
                ax.annotate(f"{f:.1f} Hz", xy=(f, a), xytext=(4, 6),
                            textcoords="offset points", fontsize=7, color="darkblue")
            ax.set_title(f"Aceleração Eixo {eixo.upper()}", fontsize=11)
            ax.set_xlabel("Frequência (Hz)")
            ax.set_ylabel("Amplitude")
            ax.legend(fontsize=8)
            ax.grid(True, linestyle='--', alpha=0.5)

        for index, (eixo, sinal) in enumerate(self.giro_sinais.items()):
            sinal = sinal[inicio_idx:fim_idx]
            freqs, espectro, picos_f, picos_a = _calcular_fft(sinal)

            ax = axes[index, 1]
            ax.plot(freqs, espectro, color="red", linewidth=0.8)
            ax.plot(picos_f, picos_a, "x", color="orange", markersize=8, label="Picos")
            for f, a in zip(picos_f, picos_a):
                ax.annotate(f"{f:.1f} Hz", xy=(f, a), xytext=(4, 6),
                            textcoords="offset points", fontsize=7, color="darkred")
            ax.set_title(f"Giroscópio Eixo {eixo.upper()}", fontsize=11)
            ax.set_xlabel("Frequência (Hz)")
            ax.set_ylabel("Amplitude")
            ax.legend(fontsize=8)
            ax.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout(rect=[0, 0, 1, 0.96])

        if salvar:
            plt.savefig(f"resultados/frequencias/{self.titulo}.png", dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()

        