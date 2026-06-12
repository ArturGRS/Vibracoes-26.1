# coding: utf-8
'''
Módulo para Análise de Sinais de Vibração/Aceleração.
Dividio por experimento, permite a analise dos dados, plotagem de fft,
identificação de modos fundamentais.
'''

from os import path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, detrend, butter, filtfilt
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class Experimento:
    
    def __init__(self, titulo: str, 
                arquivo_acelerometro: str, 
                arquivo_giroscopio: str, 
                taxa_amostragem: int,
                inicio: Optional[float] = None,
                fim: Optional[float] = None) -> None:
        
        self.acel = Path(arquivo_acelerometro)
        self.giro = Path(arquivo_giroscopio)
        self.taxa_amostragem = taxa_amostragem
        self.titulo = titulo
        self.inicio = inicio
        self.fim = fim

        self.acel_sinais: Dict[str, np.ndarray] = {}
        self.giro_sinais: Dict[str, np.ndarray] = {}
        self.tempo_acel: Optional[np.ndarray] = None
        self.tempo_giro: Optional[np.ndarray] = None

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

            if "Time (s)" in df_acel.columns:
                self.tempo_acel = df_acel["Time (s)"].values.astype(np.float64)
            if "Time (s)" in df_giro.columns:
                self.tempo_giro = df_giro["Time (s)"].values.astype(np.float64)

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

    def explorar_sinal(self, inicio: float = None, 
                fim: float = None, 
                salvar_grafico: bool = False,
                exportar_segmento: str = None) -> None:
        '''
        Visualização exploratória do sinal cru (sem transformações).
        Serve para entender o dataset e decidir onde cortar o segmento.
        Se exportar_segmento for passado, salva o recorte como CSV.
        '''
        inicio = inicio if inicio is not None else self.inicio
        fim = fim if fim is not None else self.fim

        inicio_idx = int(inicio * self.taxa_amostragem) if inicio is not None else 0
        fim_idx = int(fim * self.taxa_amostragem) if fim is not None else None

        figure, axes = plt.subplots(3, 2, figsize=(12, 9), sharey=False)
        figure.suptitle(f"{self.titulo.replace('_',' ').title()}", fontsize=14, fontweight='bold')

        for index, (eixo, sinal) in enumerate(self.acel_sinais.items()):
            sinal = sinal[inicio_idx:fim_idx]
            ax = axes[index, 0]
            if self.tempo_acel is not None:
                t = self.tempo_acel[inicio_idx:fim_idx]
            else:
                t = np.arange(len(sinal)) / self.taxa_amostragem
            ax.plot(t, sinal, color="blue", linewidth=0.5)
            ax.set_title(f"Aceleração Eixo {eixo.upper()}", fontsize=11)
            ax.set_xlabel("Tempo (s)")
            ax.set_ylabel("Amplitude (m/s²)")
            ax.grid(True, linestyle='--', alpha=0.5)

        for index, (eixo, sinal) in enumerate(self.giro_sinais.items()):
            sinal = sinal[inicio_idx:fim_idx]
            sinal = sinal[200:]
            ax = axes[index, 1]
            if self.tempo_giro is not None:
                t = self.tempo_giro[inicio_idx:fim_idx][200:]
            else:
                t = np.arange(len(sinal)) / self.taxa_amostragem
            ax.plot(t, sinal, color="red", linewidth=0.5)
            ax.set_title(f"Giroscópio Eixo {eixo.upper()}", fontsize=11)
            ax.set_xlabel("Tempo (s)")
            ax.set_ylabel("Amplitude (rad/s)")
            ax.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout(rect=[0, 0, 1, 0.96])

        if salvar_grafico:
            plt.savefig(f"resultados/sensores/{self.titulo}.png", dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()

        if exportar_segmento:
            dados = {'tempo': np.arange(fim_idx - inicio_idx if fim_idx else len(list(self.acel_sinais.values())[0]) - inicio_idx) / self.taxa_amostragem}
            for eixo in "xyz":
                dados[f"acel_{eixo}"] = self.acel_sinais[eixo][inicio_idx:fim_idx]
                dados[f"giro_{eixo}"] = self.giro_sinais[eixo][inicio_idx:fim_idx]
            pd.DataFrame(dados).to_csv(exportar_segmento, index=False)
            print(f"Segmento exportado para: {exportar_segmento}")

    def ver_fft(self, inicio: float = None,
                    fim: float = None,
                    limite_frequencia: float = 25,
                    limpar: bool = False,
                    salvar_grafico: bool = False,
                    exportar_fft: str = None) -> None:
        '''
        Calcula e plota a FFT do segmento definido.
        limpar=True aplica detrend + filtro passa-banda antes da FFT.
        exportar_fft salva os dados numéricos {frequencia, amplitude} como CSV.
        '''
        def _limpar_sinal(_sinal) -> np.ndarray:
            _sinal = detrend(_sinal)
            max_abs = np.max(np.abs(_sinal))
            if max_abs > 0:
                _sinal = _sinal / max_abs
            nyq = self.taxa_amostragem / 2
            b, a = butter(4, [1/nyq, 50/nyq], btype='band')
            return filtfilt(b, a, _sinal)

        def _calcular_fft(sinal: np.ndarray):
            n_amostras = len(sinal)
            frequencias = np.fft.rfftfreq(n_amostras, d=1.0 / self.taxa_amostragem)
            espectro = np.abs(np.fft.rfft(sinal))

            limite_ruido = np.max(espectro) * 0.05
            picos_indices, _ = find_peaks(
                espectro, height=limite_ruido,
                distance=int(n_amostras / self.taxa_amostragem)
            )

            mascara = frequencias <= limite_frequencia
            frequencias_filtradas = frequencias[mascara]
            espectro_filtrado = espectro[mascara]

            picos_validos = picos_indices[picos_indices < len(frequencias_filtradas)]
            return frequencias_filtradas, espectro_filtrado, frequencias_filtradas[picos_validos], espectro_filtrado[picos_validos]

        inicio = inicio if inicio is not None else self.inicio
        fim = fim if fim is not None else self.fim

        inicio_idx = int(inicio * self.taxa_amostragem) if inicio is not None else 0
        fim_idx = int(fim * self.taxa_amostragem) if fim is not None else None

        figure, axes = plt.subplots(3, 2, figsize=(12, 9), sharey=False)
        figure.suptitle(f"{self.titulo.replace('_',' ').title()} — Espectro de Frequências", fontsize=14, fontweight='bold')

        dados_export = {}

        for index, (eixo, sinal) in enumerate(self.acel_sinais.items()):
            sinal = sinal[inicio_idx:fim_idx]
            if limpar:
                sinal = _limpar_sinal(sinal)
            freqs, espectro, picos_f, picos_a = _calcular_fft(sinal)

            if exportar_fft:
                dados_export[f"freq_acel_{eixo}"] = freqs
                dados_export[f"amp_acel_{eixo}"] = espectro

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
            if limpar:
                sinal = _limpar_sinal(sinal)
            freqs, espectro, picos_f, picos_a = _calcular_fft(sinal)

            if exportar_fft:
                dados_export[f"freq_giro_{eixo}"] = freqs
                dados_export[f"amp_giro_{eixo}"] = espectro

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

        if salvar_grafico:
            plt.savefig(f"resultados/frequencias/{self.titulo}.png", dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()

        if exportar_fft:
            max_len = max(len(v) for v in dados_export.values())
            for k in dados_export:
                arr = dados_export[k]
                dados_export[k] = np.pad(arr, (0, max_len - len(arr)), constant_values=np.nan)
            pd.DataFrame(dados_export).to_csv(exportar_fft, index=False)
            print(f"Dados FFT exportados para: {exportar_fft}")

    @staticmethod
    def extrair_modos(
        experimentos: List['Experimento'],
        limite_frequencia: float = 25.0
    ) -> Dict[str, Dict[str, List[float]]]:
        '''
        Calcula a média dos espectros de múltiplos experimentos e retorna
        as frequências dos modos naturais detectados por eixo e sensor.
        
        Retorna:
            {
                'acelerometro': {'x': [f1, f2, ...], 'y': [...], 'z': [...]},
                'giroscopio':   {'x': [f1, f2, ...], 'y': [...], 'z': [...]}
            }
        '''
        N = 1000
        freqs_comum = np.linspace(0, limite_frequencia, N)
        espectros_acel = {eixo: [] for eixo in "xyz"}
        espectros_giro = {eixo: [] for eixo in "xyz"}

        for exp in experimentos:
            i_idx = int(exp.inicio * exp.taxa_amostragem) if exp.inicio is not None else 0
            f_idx = int(exp.fim * exp.taxa_amostragem) if exp.fim is not None else None

            for eixo in "xyz":
                sinal_acel = exp.acel_sinais[eixo][i_idx:f_idx]
                freqs_a = np.fft.rfftfreq(len(sinal_acel), d=1.0 / exp.taxa_amostragem)
                espectro_a = np.abs(np.fft.rfft(sinal_acel))
                espectros_acel[eixo].append(np.interp(freqs_comum, freqs_a, espectro_a))

                sinal_giro = exp.giro_sinais[eixo][i_idx:f_idx]
                freqs_g = np.fft.rfftfreq(len(sinal_giro), d=1.0 / exp.taxa_amostragem)
                espectro_g = np.abs(np.fft.rfft(sinal_giro))
                espectros_giro[eixo].append(np.interp(freqs_comum, freqs_g, espectro_g))

        modos = {
            'acelerometro': {},
            'giroscopio': {}
        }

        for eixo in "xyz":
            # Acelerômetro
            espectro_medio = np.mean(espectros_acel[eixo], axis=0)
            picos_idx, _ = find_peaks(espectro_medio, height=np.max(espectro_medio) * 0.05, distance=int(N / 25))
            modos['acelerometro'][eixo] = [round(float(freqs_comum[i]), 2) for i in picos_idx]

            # Giroscópio
            espectro_medio = np.mean(espectros_giro[eixo], axis=0)
            picos_idx, _ = find_peaks(espectro_medio, height=np.max(espectro_medio) * 0.05, distance=int(N / 25))
            modos['giroscopio'][eixo] = [round(float(freqs_comum[i]), 2) for i in picos_idx]

        return modos