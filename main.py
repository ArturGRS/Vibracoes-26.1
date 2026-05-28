from analise_sinais import AnalisadorVibracao

TAXA_AMOSTRAGEM = 400
LIMITE_HZ = 20

try:
    df = AnalisadorVibracao(arquivo_excel="experimento\deslocamento-atenuado\Accelerometer.csv", taxa_amostragem=TAXA_AMOSTRAGEM)
    
    for eixo_disponivel in df.sinais.keys():
        df.encontrar_modos_fundamentais(eixo=eixo_disponivel, top_n=5)
        
        df.plotar_analise(eixo=eixo_disponivel, limite_frequencia=LIMITE_HZ)
        
        df.plotar_fft(eixo=eixo_disponivel, limite_frequencia=LIMITE_HZ)
    

except FileNotFoundError:
    print("Arquivo de teste não encontrado. Verifique o caminho.")