from analise_sinais import AnalisadorVibracao

'''
Usa essa função para poder ver como que ficou o sinal de cada eixo POR arquivo

Comentário: Eu estava usando essa função para decidir qual dos eixos que eu ia usar para a anlise final...kkk
'''


if __name__ == '__main__':
    
    paths = {
        'Deslocamento Atenuado (Aceleração)': 'experimento/deslocamento-atenuado/Accelerometer.csv',    # Mantém somente o Eixo X
        'Deslocamento Atenuado (Giroscópio)': 'experimento/deslocamento-atenuado/Gyroscope.csv',        # Mantém somente o Eixo Z

        'Deslocamento Livre (Aceleração)': 'experimento/deslocamento-livre/Accelerometer.csv',          # Mantém somente o Eixo X
        'Deslocamento Livre Giro': 'experimento/deslocamento-livre/Gyroscope.csv',                      # Mantém somente o Eixo Z

        'Torção Livre (Aceleração)': 'experimento/torcao-livre/Accelerometer.csv',                      # Mantém somente o Eixo X
        'Torção Livre (Giroscópio)': 'experimento/torcao-livre/Gyroscope.csv',                          # Mantém somente o Eixo Z (esse ta lindo)
    }

    for experimento, path_file in paths.items():
        print('='*30)
        print(f'{experimento.title()}')
        print('='*30)
        df = AnalisadorVibracao(arquivo_excel=path_file, taxa_amostragem=500)
        df.plotar_todos_os_eixos_do_sinal(title = experimento)