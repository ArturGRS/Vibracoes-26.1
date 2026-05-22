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
   - 5.1 [Código — Python](#51-codigo--python)
   - 5.2 [Código — Mat Lab](#52-codigo--matlab)
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

A Análise de Vibrações é uma vertente fundamental da engenharia que visa determinar os parâmetros modais de um sistema — especificamente suas frequências naturais, modos de vibrar e coeficientes de amortecimento. A identificação precisa dessas propriedades é indispensável para prever a resposta dinâmica de sistemas estruturais quando submetidos a excitações externas, permitindo mitigar os efeitos destrutivos de fenômenos como a ressonância e a fadiga mecânica.

No escopo da dinâmica estrutural, o modelo *Shear Building* (Edifício de Cisalhamento) constitui uma idealização analítica consagrada para a simplificação do comportamento de estruturas de múltiplos pavimentos. Sob essa formulação, adota-se a hipótese de que as lajes e vigas apresentam rigidez à flexão infinitamente superior à dos pilares de sustentação. Como consequência direta dessa premissa, os deslocamentos rotacionais e verticais dos nós são desprezados, restringindo o movimento da estrutura a translações estritamente horizontais em cada nível de massa.

Dessa forma, o edifício é discretizado como um sistema de Múltiplos Graus de Liberdade (MGL), no qual a massa de cada pavimento é considerada concentrada no nível da laje e as colunas atuam como elementos elétricos de ligação (molas) que oferecem resistência ao cisalhamento horizontal. O presente trabalho documenta o desenvolvimento da modelagem matricial e computacional de um modelo *Shear Building* de quatro andares, com foco na extração de suas frequências naturais e formas modais via formulação em espaço de estados, estabelecendo os fundamentos analíticos necessários para a avaliação do comportamento dinâmico da estrutura.

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         2. METODOLOGIA           ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 2 Metodologia

Realizamos o primeiro estudo utilizando Python para clarificar a ordem de resolução do problema, focando na montagem automática das matrizes do sistema. A equação que rege o movimento de um sistema MGL sob vibração livre é dada por:

</div>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$M\ddot{x}(t) + C\dot{x}(t) + Kx(t) = 0 \tag{2.1}$$

</div>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Onde $M$ é a matriz de massa, $C$ é a matriz de amortecimento, $K$ é a matriz de rigidez e $x(t)$ é o vetor de deslocamentos. Para simplificar a análise inicial (conforme o código no Apêndice 5.1), a matriz de amortecimento foi considerada nula ($C = 0$).

A construção da matriz de rigidez global $K$ foi implementada utilizando o conceito de conectividade, similar ao Método dos Elementos Finitos (MEF). Define-se uma matriz de rigidez local para cada andar e, com base em uma matriz de nós (onde o nó 0 representa o solo fixo), os valores são somados nas posições globais correspondentes. O nó 0 tem seu grau de liberdade eliminado no código (`free_dof = total_dof[1:]`), garantindo a condição de contorno de engastamento na base.

Para encontrar as frequências naturais e os modos de vibração computacionalmente, convertemos o sistema de equações diferenciais de segunda ordem em um sistema de primeira ordem utilizando a representação em espaço de estados, onde a matriz de estado $Q$ é definida como:

</div>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$Q = \begin{bmatrix} 0 & I \\ -M^{-1}K & -M^{-1}C \end{bmatrix} \tag{2.2}$$

</div>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Após o equacionamento em Python, o problema de autovalores e autovetores foi solucionado utilizando a função `eig(Q)` da biblioteca `numpy.linalg`.

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         3. RESULTADOS            ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 3 Resultados e Implicações Físicas

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum


</div>


---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         4. CONCLUSÃO             ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 4 Conclusão

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║           5. APÊNDICE            ║ -->
<!-- ╚══════════════════════════════════╝ -->

## 5 Apêndice

### 5.1 Codigo — Python

```python
import numpy as np
from numpy.linalg import inv,eig

## DEFINIÇÕES
m1 = m2 = m3 = m4 = 1
k1 = k2 = k3 = k4 = 1

## MATRIZ DE MASSA + MATRIX
m_n = np.array([m1, m2, m3, m4])
M = np.diag(m_n)
n_massas = len(m_n)

## MATRIZ DE AMORTECIMENTO
Z = np.zeros([n_massas,n_massas])
C = Z

## MATRIZ DE CONECTIVIDADE (INPUT)
conectividade = np.array([[0,1],
                         [1,2],
                         [2,3],
                         [3,4]])


k_n = np.array([k1,k2,k3,k4])
K = np.zeros([n_massas+1,n_massas+1])

## MATRIZ DE RIGIDIZ GLOBAL SE BASEA NA CONECTIVIDADERIGIDEZ 
for k , elemento in zip(k_n,conectividade):
    k_local = np.array([[k , -k],
                       [-k , k]])
    K[np.ix_(elemento,elemento)] += k_local
total_dof = np.arange(0,n_massas+1, 1)

## ELIMINANDO O GRAU ZERO, QUE FOI CONSIDERADO O CHÃO
free_dof = total_dof[1:]
K = K[np.ix_(free_dof,free_dof)]

## AUTOVALORES E AUTOVETORES
I = np.identity(n_massas)
Q = np.block([[Z , I],
             [-inv(M) @ K , -inv(M) @ C]])
    
autovalores, autovetores = eig(Q)
print(autovalores,autovetores)
```

### 5.2 Codigo — MatLab
```MATLAB
x = 0:pi/100:2*pi;
y = sin(x);
plot(x,y)
title('Gráfico da função Seno')
xlabel('x')
ylabel('sin(x)')
```
---