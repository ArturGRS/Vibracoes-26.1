<!--
  TEMPLATE — UFSC - Geral
  UFSC · Departamento de Engenharias da Mobilidade · EMB0000
  ─────────────────────────────────────────────────────────────
  INSTRUÇÕES DE USO:
  • Substitua os blocos marcados com [PREENCHER] pelo conteúdo do seu trabalho.
  • Para inserir imagens, substitua o src="figura_X.png" pelo caminho real do arquivo.
  • As proporções e tamanhos de imagem estão definidos por width nas tags <img>.
  • Este template funciona bem no VS Code (extensão Markdown Preview Enhanced),
    Obsidian, Typora, e ao exportar para PDF via Pandoc.
-->

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║           CAPA                   ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 13pt; line-height: 1.8;">

Universidade Federal de Santa Catarina  
Departamento de Engenharias da Mobilidade  
Vibrações - EMB5115

<br><br>

<!-- Logo da instituição -->
<img src="src\img\ufsc.png" alt="Logo UFSC" width="160"/>

<br><br>

<h1 style="font-size: 18pt; font-weight: bold; font-family: 'Times New Roman', Times, serif;">
  Análise Vibratória do Modelo Shear Building
</h1>

<br><br><br><br><br>

Arthur Frederico Gouveia &nbsp;&nbsp; 21200554 <br>
Artur Gemaque Rezende da Silva &nbsp;&nbsp; 23203758

<br><br><br><br><br><br><br>

Joinville  
2026

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║           SUMÁRIO                ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

## Sumário

1. [Introdução](#1-introdução)
2. [Metodologia](#2-metodologia)
3. [Resultados](#3-resultados)
4. [Conclusão](#4-conclusão)
5. [Apêndice](#5-apêndice)
   - 5.1 [Código — Python ](#51-código--cálculo-dos-cps-e-cd-e-geração-dos-gráficos)
6. [Referências](#6-referências)

</div>

<!-- ---

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

## Lista de Figuras

| | |
|---|---|
| Figura 1 | Distribuição de C<sub>P</sub> — 7,7 m/s |
| Figura 2 | Distribuição de C<sub>P</sub> — 4,1 m/s |
| Figura 3 | Distribuição de C<sub>P</sub> — 1,8 m/s |
| Figura 4 | Previsão experimental da distribuição de C<sub>P</sub> |
| Figura 5 | Previsão experimental — C<sub>D</sub> |

</div>

---

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

## Lista de Tabelas

| | |
|---|---|
| Tabela 1 | Velocidades e Reynolds do Ensaio |
| Tabela 2 | Resultados — C<sub>D</sub> |
| Tabela 3 | Erro relativo — Previsão x Experimento |

</div> -->

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         1. INTRODUÇÃO            ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 1 Introdução

A Análise de Vibrações é um ramo da engenharia que tem como finalidade a obtenção dos parâmetros modais de uma estrutura – frequência natural, amortecimento e modos de vibração – por meio da análise de seu comportamento vibratório em resposta às forças externas que atuam sobre ela. Existem inúmeros métodos para obter esses parâmetros.

<!-- seja utilizando dados de entrada e saída, ou somente dados de saída da estrutura em estudo. Em geral, esse tipo de análise é vantajoso porque não danifica a estrutura e permite a captação de dados com a estrutura em funcionamento. -->

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         2. METODOLOGIA           ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 2 Metodologia

Nos realizamos os primeiro estudo utilizando python para clarificar a ordem de resolução do problema depois seguimos com a realização de casos utilizando o MatLab por fim seguimos realizando algumas simulações dentro Simcenter Femap para exemplificar os processos desenvolvidos nesse texto

</div><br><br>

<!-- Equação centralizada -->
<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$ \mu = \frac{1{,}485 \times 10^{-6} \, T}{1 + \left(\dfrac{110{,}4}{T}\right)} \tag{1.0}$$
</div><br><br>

<!-- Tabela 1 centralizada -->
<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin: 20px 0;">

**Tabela 1: Velocidades e Reynolds do Ensaio**
| Velocidade [m/s] | Densidade do ar [kg/m³] | Re |
|:-:|:-:|:-:|
| 7,7 | 1,32 | 8,28E04 |
| 4,1 | 1,49 | 5,00E04 |
| 1,8 | 1,73 | 2,55E04 |
</div><br><br>


<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Foi implementado um script em Python a fim de calcular os C<sub>P</sub>'s para cada uma das 20 leituras ao longo da meia circunferência do cilindro, nos três casos de velocidade. Em seguida, foram obtidos os valores médios para cada ponto analisado do cilindro.

Uma vez obtida a distribuição de C<sub>P</sub> ao longo do cilindro, foi possível calcular o Coeficiente de Arrasto C<sub>D</sub> do mesmo. Analogamente à solução analítica do C<sub>D</sub>, foi realizada uma integração numérica dos valores C<sub>P</sub> cos(θ) em cada respectivo θ, utilizando o método do trapézio.

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         3. RESULTADOS            ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 3 Resultados

Após a integração, foram obtidos os C<sub>D</sub>'s do cilindro em cada caso, apresentados na Tabela 2. Os valores de C<sub>P</sub> obtidos são mostrados a partir da Figura 1, juntamente com o desvio padrão das leituras em cada ponto, comparando com a previsão analítica do escoamento potencial, dada pela expressão C<sub>P</sub> = 2cos(2θ) − 1.

</div>

<!-- Tabela 2 centralizada -->
<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin: 20px 0;">

**Tabela 2: Resultados — C<sub>D</sub>**

| Velocidade [m/s] | 7,7 | 4,1 | 1,8 |
|:-:|:-:|:-:|:-:|
| C<sub>D</sub> | 0,629 | 0,744 | 0,612 |

</div>

<!-- Figura 1 -->
<div align="center" style="margin: 24px 0;">
  <img src="figura_1.png" alt="Distribuição de CP - 7,7 m/s" width="480"/>
  <br>
  <span style="font-family: 'Times New Roman', Times, serif; font-size: 11pt;">
    <em>Figura 1: Distribuição de C<sub>P</sub> — 7,7 m/s</em>
  </span>
</div>

<!-- Figura 2 -->
<div align="center" style="margin: 24px 0;">
  <img src="figura_2.png" alt="Distribuição de CP - 4,1 m/s" width="480"/>
  <br>
  <span style="font-family: 'Times New Roman', Times, serif; font-size: 11pt;">
    <em>Figura 2: Distribuição de C<sub>P</sub> — 4,1 m/s</em>
  </span>
</div>

<!-- Figura 3 -->
<div align="center" style="margin: 24px 0;">
  <img src="figura_3.png" alt="Distribuição de CP - 1,8 m/s" width="480"/>
  <br>
  <span style="font-family: 'Times New Roman', Times, serif; font-size: 11pt;">
    <em>Figura 3: Distribuição de C<sub>P</sub> — 1,8 m/s</em>
  </span>
</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         4. CONCLUSÃO             ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 4 Conclusão

Nos gráficos obtidos no experimento, é possível perceber que a distribuição de C<sub>P</sub> obtida experimentalmente difere de forma significativa do proposto pelo modelo potencial. Isso se dá devido a uma hipótese base do mesmo: a hipótese de inviscidade citada anteriormente. Como a viscosidade ainda é presente, apesar de pequena no caso do ar, o escoamento perde energia conforme percorre a superfície do cilindro devido ao atrito viscoso, até o ponto em que ocorre o descolamento da camada limite.

Além disso, também é possível notar que quanto mais laminar é o escoamento, mais a distribuição de C<sub>P</sub>'s difere do proposto pelo modelo potencial, tendendo a "planificar" cada vez mais cedo. Tal fenômeno pode ser explicado pela própria definição do número de Reynolds: quanto menor ele é, mais os efeitos viscosos predominam, fugindo do modelo potencial. Esse comportamento é coerente com a previsão experimental apresentada por Munson (MUNSON; OKIISHI; YOUNG, 1997).

</div>

<!-- Figura 4 -->
<div align="center" style="margin: 24px 0;">
  <img src="figura_4.png" alt="Previsão experimental da distribuição de CP" width="360"/>
  <br>
  <span style="font-family: 'Times New Roman', Times, serif; font-size: 11pt;">
    <em>Figura 4: Previsão experimental da distribuição de C<sub>P</sub></em>
  </span>
</div>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Pode-se perceber também que os valores de C<sub>D</sub> ficaram abaixo da previsão experimental para um cilindro liso. Acredita-se que as tomadas de pressão ao longo do cilindro, junto com os geradores de vórtice colocados no mesmo, tenham causado tal discrepância com a previsão experimental, também apresentada por Munson.

</div>

<!-- Tabela 3 centralizada -->
<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin: 20px 0;">

**Tabela 3: Erro relativo — Previsão x Experimento**

| Reynolds | 8,28E04 | 5,00E04 | 2,55E04 |
|:-:|:-:|:-:|:-:|
| Erro relativo* | 58,1% | 50,4% | 59,2% |

<span style="font-size: 10pt;">* Erro aproximado, considerado C<sub>D</sub> previsto como 1,5</span>

</div>

<!-- Figura 5 -->
<div align="center" style="margin: 24px 0;">
  <img src="figura_5.png" alt="Previsão experimental - CD" width="420"/>
  <br>
  <span style="font-family: 'Times New Roman', Times, serif; font-size: 11pt;">
    <em>Figura 5: Previsão experimental — C<sub>D</sub></em>
  </span>
</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║           5. APÊNDICE            ║ -->
<!-- ╚══════════════════════════════════╝ -->

## 5 Apêndice

### 5.1 Código — Cálculo dos Cp's e Cd, e geração dos gráficos

```python
import pandas as pd
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

def Reynolds(rho, v, D, mu):
    return rho * float(v) * D / mu

def Cp_analitico(theta):
    return 2 * np.cos(2 * theta) - 1

def Solve(data, v):
    P_med = []
    Cp_med = []
    Desv_pad = []

    for col in data:
        P_med.append(data[col].mean())  # Obtendo os valores médios de pressão

    rho = densidade(P_med[0], v)  # Cálculo da densidade do ar

    for col in data:
        Cp = []
        for i in range(len(data)):
            Cp.append(2 * data.loc[i, col] / (rho * float(v)**2))
        Cp_med.append(np.mean(Cp))
        Desv_pad.append(np.std(Cp))

    Cp_med = np.array(Cp_med)
    Desv_pad = np.array(Desv_pad)

    return Cp_med, Desv_pad, rho

def densidade(p, v):
    rho = 2 * p / float(v)**2
    print("Densidade do ar " + v + " m/s = ", rho)
    return rho

def graph(Cp_med, Desv_pad, x_rad, x, v, Re, rho, CD):
    y_analitico = [Cp_analitico(theta) for theta in x_rad]
    y_analitico = np.array(y_analitico)

    plt.plot(x, y_analitico, color='red', label='Cp analítico')
    plt.title("Vel = " + v + " m/s", fontweight='bold')
    plt.ylabel("Cp", rotation=0, labelpad=10, fontweight='bold')
    plt.xlabel("(°)", fontweight='bold')
    plt.errorbar(x, Cp_med, Desv_pad, fmt='o', capsize=7,
                 markersize=4, label='Cp experimental')
    plt.legend()
    plt.text(0.025, 0.17, f'rho = {rho:.2f} kg/m³',
             transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='bottom', horizontalalignment='left',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
    plt.text(0.025, 0.24, f'Re = {Re:.2e}',
             transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='bottom', horizontalalignment='left',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
    plt.text(0.025, 0.31, f'CD = {CD:.3f}',
             transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='bottom', horizontalalignment='left',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
    plt.savefig("Gráfico - " + v + ".png", dpi=300)
    plt.show()

if __name__ == '__main__':
    arquivos = ["Vel7.7.csv", "Vel4.1.csv", "Vel1.8.csv"]
    vel = ["7.7", "4.1", "1.8"]
    mu = 1.837E-05   # Viscosidade dinâmica [Pa·s]
    D = 0.15         # Diâmetro do cilindro [m]

    for adress, v in zip(arquivos, vel):
        data = pd.read_csv(adress)
        theta = [float(d.removesuffix('°')) for d in data]
        theta_rad = np.deg2rad(theta)

        Cp_medio, Desvio_padrao, rho = Solve(data, v)
        Re = Reynolds(rho, v, D, mu)
        print("Re = ", format(Re, ".2e"))

        CD = sci.integrate.trapezoid(Cp_medio * np.cos(theta_rad), theta_rad)
        print("CD " + v + " m/s = ", CD, "\n")

        graph(Cp_medio, Desvio_padrao, theta_rad, theta, v, Re, rho, CD)
```

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║          6. REFERÊNCIAS          ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; line-height: 1.8;">

## 6 Referências

ANDERSON, J. **Fundamentals of Aerodynamics**. McGraw-Hill Companies, 2017. (McGraw-Hill Aeronautical and Aerospace Engineering Series). ISBN 9780070016804.

MUNSON, B.; OKIISHI, T.; YOUNG, D. **Fundamentos da mecânica dos fluidos**. Edgard Blucher, 1997. ISBN 9788521201427.

SADRAEY, M. **Aircraft Performance: An Engineering Approach**. CRC Press, 2017. ISBN 9781498776554.

</div>