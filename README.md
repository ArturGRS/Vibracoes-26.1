# Vibrações — EMB5115 · Análise Vibratória do Modelo Shear Building

Códigos e dados experimentais do trabalho. O **relatório escrito é mantido no Overleaf** (LaTeX) — este repositório guarda apenas o que é executável e os dados.

## Estrutura

```
shear_building.py     Análise modal (autovalores) do shear building 4 GDL — Python/NumPy
shear_building.m      Mesma análise em MATLAB
analise_sinais.py     Análise de sinais de acelerômetro (FFT, espectrograma, export WAV)

experimento/          Dados medidos (export Phyphox)
  deslocamento-livre/      Accelerometer.csv, Gyroscope.csv, meta/
  deslocamento-atenuado/
  torcao-livre/
resultados/
  Conclusoes.md            Análises e conclusões dos ensaios
```

## Como rodar

- **Teórico (Python):** `python shear_building.py` — imprime frequências naturais e formas modais.
- **Teórico (MATLAB):** abrir `shear_building.m` e executar.
- **Experimental:** `python analise_sinais.py` — requer `pandas`, `numpy`, `scipy`, `matplotlib`, `librosa`.

## Roadmap 

- [ ] Realizar os experimentos do Shear Build

  1. Realizar a captação utilizando **Phyphox**
  2. Repetir 3 vezes por experimento 

- [ ] Extrair parâmetros modais experimentais. Rodar FFT dos 3 ensaios; frequências de pico = modos medidos. Comparar **deslocamento-livre × deslocamento-atenuado** para evidenciar o efeito do pêndulo/absorvedor de vibração. Tratar a *torção-livre* como caso à parte (modo fora do shear building puro).

- [ ] Documentar no Overleaf. Nova seção "Validação Experimental" no relatório; incluir `analise_sinais.py` no apêndice de código.
