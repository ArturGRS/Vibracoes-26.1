from experimento import Experimento

if __name__ == '__main__':
    
    deslocamento_livre__x_1 = Experimento(
                                    titulo='deslocamento_livre__x_1',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/delocamento-livre/exp1-x/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/delocamento-livre/exp1-x/Gyroscope.csv',
                                    taxa_amostragem=400)
    deslocamento_livre__x_2 = Experimento(
                                    titulo='deslocamento_livre__x_2',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/delocamento-livre/exp2-x/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/delocamento-livre/exp2-x/Gyroscope.csv',
                                    taxa_amostragem=400)
    deslocamento_livre__x_3 = Experimento(
                                    titulo='deslocamento_livre__x_3',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/delocamento-livre/exp3-x/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/delocamento-livre/exp3-x/Gyroscope.csv',
                                    taxa_amostragem=400)



    torcao_livre_1 = Experimento(
                                    titulo='torcao_livre_1',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/torcao-livre/exp1/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/torcao-livre/exp1/Gyroscope.csv',
                                    taxa_amostragem=400)
    torcao_livre_2 = Experimento(
                                    titulo='torcao_livre_2',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/torcao-livre/exp2/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/torcao-livre/exp2/Gyroscope.csv',
                                    taxa_amostragem=400)
    torcao_livre_3 = Experimento(
                                    titulo='torcao_livre_3',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/torcao-livre/exp3/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/torcao-livre/exp3/Gyroscope.csv',
                                    taxa_amostragem=400)



    deslocamento_atenuado_y_1 = Experimento(
                                    titulo='deslocamento_atenuado_y_1',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/deslocamento-atenuado/exp2-9cm-y/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/deslocamento-atenuado/exp2-9cm-y/Gyroscope.csv',
                                    taxa_amostragem=400)
    deslocamento_atenuado_y_2 = Experimento(
                                    titulo='deslocamento_atenuado_y_2',
                                    arquivo_acelerometro='experimento/Tavim-Moleques/deslocamento-atenuado/exp3-9cm-y/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Tavim-Moleques/deslocamento-atenuado/exp3-9cm-y/Gyroscope.csv',
                                    taxa_amostragem=400)



    deslocamento_atenuado_y_1_arthur = Experimento(
                                    titulo='deslocamento_atenuado_y_2_arthur',
                                    arquivo_acelerometro='experimento/Arthur-Frederico/deslocamento-atenuado/Accelerometer.csv',
                                    arquivo_giroscopio='experimento/Arthur-Frederico/deslocamento-atenuado/Gyroscope.csv',
                                    taxa_amostragem=500)

    # Vamos tentar pegar 50 [s]

    deslocamento_livre__x_1.ver_frequencias(inicio=10,fim=60)
    deslocamento_livre__x_2.ver_frequencias(inicio=10,fim=60)
    deslocamento_livre__x_3.ver_frequencias(inicio=10,fim=60)

    torcao_livre_1.ver_frequencias(inicio=10,fim=50)
    torcao_livre_2.ver_frequencias(inicio=6.5,fim=43)
    torcao_livre_3.ver_frequencias(inicio=5,fim=50)

    # deslocamento_atenuado_y_1.ver_frequencias(inicio=10,fim=45) # TA CAGADO
    deslocamento_atenuado_y_2.ver_frequencias(inicio=5.5,fim=72) 

    # deslocamento_atenuado_y_1_arthur.ver_frequencias() #não ta mais bonito