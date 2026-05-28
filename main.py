from analise_sinais import AnalisadorVibracao

try:
    df = AnalisadorVibracao(arquivo_excel="experimento\deslocamento-livre\Gyroscope.csv", taxa_amostragem=100)
    
    for eixo_disponivel in df.sinais.keys():
        #df.encontrar_modos_fundamentais(eixo=eixo_disponivel, top_n=5)
        df.plotar_analise(eixo=eixo_disponivel, limite_frequencia=50)
        #df.plotar_fft(eixo=eixo_disponivel, limite_frequencia=20)
    

except FileNotFoundError:
    print("Arquivo de teste não encontrado. Verifique o caminho.")