from experimento import Experimento

if __name__ == '__main__':

    exp_1 = Experimento(arquivo_acelerometro = 'experimento/deslocamento-livre/Accelerometer.csv', 
                        arquivo_giroscopio = 'experimento/deslocamento-livre/Gyroscope.csv',
                        titulo = 'deslocamento_livre',
                        taxa_amostragem = 500)


    exp_2 = Experimento(arquivo_acelerometro = 'experimento/deslocamento-atenuado/Accelerometer.csv', 
                        arquivo_giroscopio = 'experimento/deslocamento-atenuado/Gyroscope.csv',
                        titulo = 'deslocamento_atenuado',
                        taxa_amostragem = 500)


    exp_3 = Experimento(arquivo_acelerometro = 'experimento/torcao-livre/Accelerometer.csv', 
                        arquivo_giroscopio = 'experimento/torcao-livre/Gyroscope.csv',
                        titulo = 'torcao_livre',
                        taxa_amostragem = 500)

    # exp_1.ver_frequencias(inicio=1.5, fim = 60, limite_frequencia=10)
    # exp_2.ver_frequencias(inicio=3.5,fim=30)
    # exp_3.ver_frequencias(limite_frequencia=10)
    # exp_1.ver_dados()
    exp_1.calculo_amortecimento()
