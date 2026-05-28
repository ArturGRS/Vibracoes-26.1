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

## Roadmap — integrar o experimento ao relatório

- [x] **Fase 0 — Organização.** Códigos numa camada só, dados experimentais em `experimento/`, análises em `resultados/`, relatório `.tex` movido para o Overleaf (fonte única). Removidas duplicatas (`Vib_Shear_Building.md`, `src/Vibra.py` com conflito de merge não resolvido).

- [ ] **Fase 1 — Ler os dados reais.** Hoje `analise_sinais.py` lê `data/*.xls` via `pd.read_excel`. Os dados em `resultados/experimento/` são **CSV (Phyphox)** — as colunas já batem (`"Acceleration y (m/s^2)"`), basta trocar para `pd.read_csv` e apontar para as 3 pastas. Derivar a **taxa de amostragem da coluna `"Time (s)"`** (≈ 500 Hz nos ensaios) em vez do valor fixo de 400 Hz.

- [ ] **Fase 2 — Extrair parâmetros modais experimentais.** Rodar FFT dos 3 ensaios; frequências de pico = modos medidos. Comparar **deslocamento-livre × deslocamento-atenuado** para evidenciar o efeito do pêndulo/absorvedor de vibração. Tratar a *torção-livre* como caso à parte (modo fora do shear building puro).

- [ ] **Fase 3 — Validação cruzada.** Estender a tabela de frequências do relatório com a coluna experimental: **Python × MATLAB × Femap × Experimento**. Salvar os gráficos novos (FFT/espectrograma) em `resultados/` e registrar as conclusões em `resultados/Conclusoes.md`.

- [ ] **Fase 4 — Documentar no Overleaf.** Nova seção "Validação Experimental" no relatório; incluir `analise_sinais.py` no apêndice de código.
