from experimento import Experimento
from dados import deslocamento_livre_x, torcao_livre

if __name__ == '__main__':
 
    # # --- Extração dos Modos Naturais ---
    print("\n--- Modos Naturais: Deslocamento Livre X ---")

    modos_desloc = Experimento.extrair_modos(deslocamento_livre_x, limite_frequencia=25)

    for sensor, eixos in modos_desloc.items():
        print(f"  {sensor}:")
        for eixo, freqs in eixos.items():
            print(f"    Eixo {eixo.upper()}: {freqs} Hz")

    print("\n--- Modos Naturais: Torção Livre ---")
    modos_torcao = Experimento.extrair_modos(torcao_livre, limite_frequencia=25)

    for sensor, eixos in modos_torcao.items():
        print(f"  {sensor}:")
        for eixo, freqs in eixos.items():
            print(f"    Eixo {eixo.upper()}: {freqs} Hz")