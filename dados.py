# coding: utf-8
'''
Definição dos experimentos e seus parâmetros.
Cada grupo é uma lista de Experimento com o mesmo tipo de ensaio.
'''

from experimento import Experimento

# ============================================================
#                    Tavim-Moleques
# ============================================================

# --- Deslocamento Livre (Eixo X) ---
deslocamento_livre_x = [
    Experimento(
        titulo='deslocamento_livre__x_1',
        arquivo_acelerometro='experimento/Tavim-Moleques/delocamento-livre/exp1-x/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/delocamento-livre/exp1-x/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=10,
        fim=60),
    Experimento(
        titulo='deslocamento_livre__x_2',
        arquivo_acelerometro='experimento/Tavim-Moleques/delocamento-livre/exp2-x/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/delocamento-livre/exp2-x/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=10,
        fim=60),
    Experimento(
        titulo='deslocamento_livre__x_3',
        arquivo_acelerometro='experimento/Tavim-Moleques/delocamento-livre/exp3-x/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/delocamento-livre/exp3-x/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=10,
        fim=60),
]

# --- Deslocamento Livre (Eixo Y) ---
deslocamento_livre_y = [
    Experimento(
        titulo='deslocamento_livre__y_1',
        arquivo_acelerometro='experimento/Tavim-Moleques/delocamento-livre/exp4-y/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/delocamento-livre/exp4-y/Gyroscope.csv',
        taxa_amostragem=400),
]

# --- Torção Livre ---
torcao_livre = [
    Experimento(
        titulo='torcao_livre_1',
        arquivo_acelerometro='experimento/Tavim-Moleques/torcao-livre/exp1/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/torcao-livre/exp1/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=10,
        fim=50),
    Experimento(
        titulo='torcao_livre_2',
        arquivo_acelerometro='experimento/Tavim-Moleques/torcao-livre/exp2/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/torcao-livre/exp2/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=6.5,
        fim=43),
    Experimento(
        titulo='torcao_livre_3',
        arquivo_acelerometro='experimento/Tavim-Moleques/torcao-livre/exp3/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/torcao-livre/exp3/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=5,
        fim=50),
]

# --- Deslocamento Atenuado (Eixo X) ---
deslocamento_atenuado_x = [
    Experimento(
        titulo='deslocamento_atenuado_x_1',
        arquivo_acelerometro='experimento/Tavim-Moleques/deslocamento-atenuado/exp1-9cm-x/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/deslocamento-atenuado/exp1-9cm-x/Gyroscope.csv',
        taxa_amostragem=400),
]

# --- Deslocamento Atenuado (Eixo Y) ---
deslocamento_atenuado_y = [
    Experimento(
        titulo='deslocamento_atenuado_y_1',
        arquivo_acelerometro='experimento/Tavim-Moleques/deslocamento-atenuado/exp2-9cm-y/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/deslocamento-atenuado/exp2-9cm-y/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=10,
        fim=45),
    Experimento(
        titulo='deslocamento_atenuado_y_2',
        arquivo_acelerometro='experimento/Tavim-Moleques/deslocamento-atenuado/exp3-9cm-y/Accelerometer.csv',
        arquivo_giroscopio='experimento/Tavim-Moleques/deslocamento-atenuado/exp3-9cm-y/Gyroscope.csv',
        taxa_amostragem=400,
        inicio=5.5,
        fim=72),
]

# ============================================================
#                   Arthur-Frederico
# ============================================================

# --- Deslocamento Livre (Arthur) ---
deslocamento_livre_arthur = [
    Experimento(
        titulo='deslocamento_livre_arthur',
        arquivo_acelerometro='experimento/Arthur-Frederico/deslocamento-livre/Accelerometer.csv',
        arquivo_giroscopio='experimento/Arthur-Frederico/deslocamento-livre/Gyroscope.csv',
        taxa_amostragem=500),
]

# --- Torção Livre (Arthur) ---
torcao_livre_arthur = [
    Experimento(
        titulo='torcao_livre_arthur',
        arquivo_acelerometro='experimento/Arthur-Frederico/torcao-livre/Accelerometer.csv',
        arquivo_giroscopio='experimento/Arthur-Frederico/torcao-livre/Gyroscope.csv',
        taxa_amostragem=500),
]

# --- Deslocamento Atenuado (Arthur) ---
deslocamento_atenuado_arthur = [
    Experimento(
        titulo='deslocamento_atenuado_arthur',
        arquivo_acelerometro='experimento/Arthur-Frederico/deslocamento-atenuado/Accelerometer.csv',
        arquivo_giroscopio='experimento/Arthur-Frederico/deslocamento-atenuado/Gyroscope.csv',
        taxa_amostragem=500),
]
