# coding: utf-8
"""
Módulo para Análise de Sinais de Vibração/Aceleração.
Permite a extração de dados de planilhas, exportação para áudio (WAV),
análise de espectro e identificação de modos fundamentais.
"""

import pandas as pd
import numpy as np
import librosa as lb
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class AnalisadorVibracao:

    def __init__(self, arquivo_excel: str, taxa_amostragem: int = 400):
        """
        Inicializa o analisador lendo o arquivo Excel e pré-processando os sinais.
        
        :param arquivo_excel: Caminho para o arquivo Excel (.xls ou .xlsx).
        :param taxa_amostragem: Taxa de amostragem do sinal em Hz (padrão: 400).
        """
        self.arquivo_excel = Path(arquivo_excel)
        self.taxa_amostragem = taxa_amostragem
        self.sinais: Dict[str, np.ndarray] = {}
        
        # Colunas padrão mapeadas para os eixos
        self._mapa_colunas = {
        #    "x": "Acceleration x (m/s^2)",
            "y": "Acceleration y (m/s^2)",
        #    "z": "Acceleration z (m/s^2)"
        }
        
        self._carregar_dados()

    def _carregar_dados(self) -> None:
        """
        Método interno que lê a planilha, limpa NaNs e normaliza os sinais 
        para o intervalo float [-1.0, 1.0], mantendo-os na memória.
        """
        print(f"[{self.__class__.__name__}] Lendo dados de: {self.arquivo_excel.name}")
        #df = pd.read_excel(self.arquivo_excel)
        df = pd.read_csv(self.arquivo_excel)

        for eixo, nome_coluna in self._mapa_colunas.items():
            if nome_coluna in df.columns:
                # Extração e limpeza de dados nulos
                sinal = df[nome_coluna].dropna().values.astype(np.float64)
                
                # Normalização para a escala [-1.0, 1.0]
                max_abs_val = np.max(np.abs(sinal))
                if max_abs_val > 0:
                    sinal_normalizado = sinal / max_abs_val
                else:
                    sinal_normalizado = sinal
                    
                self.sinais[eixo] = sinal_normalizado
                print(f"  -> Eixo {eixo.upper()} carregado com sucesso ({len(sinal)} amostras).")

    def exportar_para_wav(self, diretorio_saida: str = ".") -> List[Path]:
        """
        Converte os sinais armazenados em memória para arquivos WAV de 16-bit PCM.
        
        :param diretorio_saida: Pasta onde os arquivos serão salvos.
        :return: Lista com os caminhos dos arquivos gerados.
        """
        dir_out = Path(diretorio_saida)
        dir_out.mkdir(parents=True, exist_ok=True)
        arquivos_gerados = []

        for eixo, sinal in self.sinais.items():
            # Conversão da escala float [-1, 1] para int16
            audio_data = np.int16(sinal * 32767)
            
            nome_arquivo = f"sinal_aceleracao_eixo_{eixo}.wav"
            caminho_completo = dir_out / nome_arquivo
            
            wavfile.write(caminho_completo, self.taxa_amostragem, audio_data)
            arquivos_gerados.append(caminho_completo)
            print(f"[{self.__class__.__name__}] Arquivo exportado: {caminho_completo}")
            
        return arquivos_gerados

    def plotar_analise(self, eixo: str, limite_frequencia: Optional[float] = None) -> None:
        """
        Plota a forma de onda e o espectrograma do eixo selecionado.
        
        :param eixo: Eixo a ser analisado ('x', 'y' ou 'z').
        :param limite_frequencia: Limite máximo do eixo Y (frequência em Hz) no espectrograma.
        """
        eixo = eixo.lower()
        if eixo not in self.sinais:
            print(f"Erro: Dados do eixo '{eixo}' não estão disponíveis.")
            return

        sinal = self.sinais[eixo]
        print(f"[{self.__class__.__name__}] Gerando gráficos para o Eixo {eixo.upper()}...")

        plt.figure(figsize=(15, 5))

        # --- Gráfico 1: Forma de Onda ---
        plt.subplot(1, 2, 1)
        lb.display.waveshow(sinal, sr=self.taxa_amostragem, color="blue")
        plt.title(f"Eixo {eixo.upper()}: Forma de Onda")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Amplitude Normalizada")

        # --- Gráfico 2: Espectrograma ---
        plt.subplot(1, 2, 2)
        stft = lb.stft(sinal)
        espectrograma = lb.amplitude_to_db(np.abs(stft), ref=np.max)
        
        img = lb.display.specshow(
            espectrograma, 
            x_axis='time', 
            y_axis='linear', 
            sr=self.taxa_amostragem
        )
        plt.colorbar(img, format="%+2.0f dB")
        plt.title(f"Eixo {eixo.upper()}: Espectrograma")
        
        # --- NOVO: Aplica o limite de frequência no Eixo Y ---
        if limite_frequencia is not None:
            plt.ylim(0, limite_frequencia)

        plt.tight_layout()
        plt.show()

    def encontrar_modos_fundamentais(self, eixo: str, top_n: int = 5) -> Optional[List[Tuple[float, float]]]:
        """
        Aplica a FFT ao sinal do eixo especificado e retorna as frequências 
        com maior amplitude (modos fundamentais).
        
        :param eixo: Eixo a ser analisado ('x', 'y' ou 'z').
        :param top_n: Número de modos a serem exibidos.
        :return: Lista de tuplas contendo (frequência, amplitude) ou None se falhar.
        """
        eixo = eixo.lower()
        if eixo not in self.sinais:
            print(f"Erro: Dados do eixo '{eixo}' não estão disponíveis.")
            return None

        print(f"\n[{self.__class__.__name__}] Analisando FFT para o Eixo {eixo.upper()}...")
        sinal = self.sinais[eixo]
        n_amostras = len(sinal)
        
        # Cálculo da FFT
        frequencias = np.fft.rfftfreq(n_amostras, d=1.0/self.taxa_amostragem)
        espectro_amplitude = np.abs(np.fft.rfft(sinal))
        
        # Identificação de picos
        limite_ruido = np.max(espectro_amplitude) * 0.05
        picos_indices, propriedades = find_peaks(
            espectro_amplitude, 
            height=limite_ruido, 
            distance=int(n_amostras / self.taxa_amostragem)
        )
        
        frequencias_picos = frequencias[picos_indices]
        amplitudes_picos = propriedades['peak_heights']
        
        # Ordenação decrescente de amplitude
        indices_ordenados = np.argsort(amplitudes_picos)[::-1]
        
        print("-" * 45)
        print(f"{'Ranking':<10} | {'Frequência (Hz)':<15} | {'Amplitude Relativa'}")
        print("-" * 45)
        
        resultados = []
        for i in range(min(top_n, len(indices_ordenados))):
            idx = indices_ordenados[i]
            freq_hz = frequencias_picos[idx]
            amp = amplitudes_picos[idx]
            resultados.append((freq_hz, amp))
            
            print(f"Modo {i+1:<5} | {freq_hz:>10.3f} Hz   | {amp:>10.1f}")
            
        print("-" * 45)
        return resultados

    def plotar_fft(self, eixo: str, limite_frequencia: Optional[float] = None) -> None:
        """
        Calcula e plota o gráfico do espectro de frequências (FFT) do sinal.
        
        :param eixo: Eixo a ser analisado ('x', 'y' ou 'z').
        :param limite_frequencia: Limite máximo do eixo X no gráfico (em Hz). 
                                  Se None, mostra até a frequência de Nyquist.
        """
        eixo = eixo.lower()
        if eixo not in self.sinais:
            print(f"Erro: Dados do eixo '{eixo}' não estão disponíveis.")
            return

        print(f"[{self.__class__.__name__}] Gerando gráfico da FFT para o Eixo {eixo.upper()}...")
        sinal = self.sinais[eixo]
        n_amostras = len(sinal)
        
        # Cálculo da FFT
        frequencias = np.fft.rfftfreq(n_amostras, d=1.0/self.taxa_amostragem)
        espectro_amplitude = np.abs(np.fft.rfft(sinal))
        
        # Criação do gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(frequencias, espectro_amplitude, color='purple', alpha=0.8)
        
        # Encontra e marca os picos principais para facilitar a visualização
        limite_ruido = np.max(espectro_amplitude) * 0.05
        picos_indices, _ = find_peaks(
            espectro_amplitude, 
            height=limite_ruido, 
            distance=int(n_amostras / self.taxa_amostragem)
        )
        
        # Destaca os picos no gráfico
        plt.plot(frequencias[picos_indices], espectro_amplitude[picos_indices], "x", color='red', markersize=8, label="Picos/Modos")
        
        plt.title(f"Espectro de Frequência (FFT) - Eixo {eixo.upper()}")
        plt.xlabel("Frequência (Hz)")
        plt.ylabel("Amplitude")
        
        # Limita o eixo X se o usuário quiser focar nas baixas frequências (ex: 0 a 50 Hz)
        if limite_frequencia is not None:
            plt.xlim(0, limite_frequencia)
            
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()


# ==========================================
# Exemplo de Uso (Ponto de Entrada)
# ==========================================
if __name__ == "__main__":

    TAXA_AMOSTRAGEM = 400
    LIMITE_HZ = 20
    
    try:
        Sem_pendulo = AnalisadorVibracao(arquivo_excel="data/Acelerao com g 2026-05-26 09-42-26.xls", taxa_amostragem=TAXA_AMOSTRAGEM)
        Com_pendulo = AnalisadorVibracao(arquivo_excel="data/Acelerao com g 2026-05-26 09-37-59(Com pêndulo).xls", taxa_amostragem=TAXA_AMOSTRAGEM)
        
        for eixo_disponivel in Sem_pendulo.sinais.keys():
            Sem_pendulo.encontrar_modos_fundamentais(eixo=eixo_disponivel, top_n=5)
            Com_pendulo.encontrar_modos_fundamentais(eixo=eixo_disponivel, top_n=5)        
            
            Sem_pendulo.plotar_analise(eixo=eixo_disponivel, limite_frequencia=LIMITE_HZ)
            Com_pendulo.plotar_analise(eixo=eixo_disponivel, limite_frequencia=LIMITE_HZ)            
            
            Sem_pendulo.plotar_fft(eixo=eixo_disponivel, limite_frequencia=LIMITE_HZ)
            Com_pendulo.plotar_fft(eixo=eixo_disponivel, limite_frequencia=LIMITE_HZ)
        

    except FileNotFoundError:
        print("Arquivo de teste não encontrado. Verifique o caminho.")