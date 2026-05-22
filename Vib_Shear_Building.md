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
   - 2.1 [Modelo Estrutural — Shear Building](#21-modelo-estrutural--shear-building)
   - 2.2 [Formulação Matemática](#22-formulação-matemática)
   - 2.3 [Formulação em Espaço de Estados](#23-formulação-em-espaço-de-estados)
   - 2.4 [Análise de Autovalores](#24-análise-de-autovalores)
3. [Implementação Computacional](#3-implementação-computacional)
4. [Resultados](#4-resultados)
5. [Conclusão](#5-conclusão)
6. [Apêndice](#6-apêndice)
   - 6.1 [Código — Python](#61-código--python)
7. [Referências](#7-referências)

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         1. INTRODUÇÃO            ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 1 Introdução

A Análise de Vibrações é um ramo da engenharia que tem como finalidade a obtenção dos parâmetros modais de uma estrutura — frequência natural, amortecimento e modos de vibração — por meio da análise de seu comportamento vibratório em resposta às forças externas que atuam sobre ela. Existem inúmeros métodos para obter esses parâmetros, seja utilizando dados de entrada e saída, ou somente dados de saída da estrutura em estudo. Em geral, esse tipo de análise é vantajoso porque não danifica a estrutura e permite a captação de dados com a estrutura em funcionamento.

No contexto da engenharia civil e sísmica, o modelo de **Shear Building** (edifício cisalhante) é amplamente utilizado para representar o comportamento dinâmico lateral de edificações de múltiplos andares. Trata-se de uma idealização que concentra as massas nos pisos e representa a rigidez lateral das colunas como molas lineares, permitindo uma análise modal eficiente com boa acurácia para as primeiras frequências naturais da estrutura.

O presente trabalho descreve a formulação teórica e a implementação computacional da análise modal de um shear building de 4 andares utilizando a linguagem Python. O problema é formulado no espaço de estados, e os parâmetros modais — frequências naturais e formas modais — são obtidos por meio da decomposição em autovalores e autovetores da matriz de estado do sistema.

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         2. METODOLOGIA           ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 2 Metodologia

### 2.1 Modelo Estrutural — Shear Building

O modelo de shear building é uma idealização estrutural baseada nas seguintes hipóteses:

- As **massas** são concentradas nos pisos (lajes), representando a inércia translacional de cada andar;
- As **lajes são infinitamente rígidas**, de modo que não há rotação relativa entre os nós;
- A **rigidez lateral** de cada conjunto de colunas entre dois andares é representada por uma mola linear equivalente de rigidez $k_i$;
- O sistema possui apenas **graus de liberdade translacionais** horizontais.

A estrutura modelada possui 4 andares e base fixa, conforme a Figura 1. Os nós são numerados de 0 (base fixa) a 4 (topo). A condição de contorno de base fixa elimina o grau de liberdade do nó 0, resultando em um sistema com **4 graus de liberdade** livres.

---

### 2.2 Formulação Matemática

A equação de movimento do sistema discreto com $n$ graus de liberdade é:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{M}\ddot{\mathbf{x}} + \mathbf{C}\dot{\mathbf{x}} + \mathbf{K}\mathbf{x} = \mathbf{f}(t) \tag{2.1}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

onde $\mathbf{M}$, $\mathbf{C}$ e $\mathbf{K}$ são as matrizes de massa, amortecimento e rigidez; $\mathbf{x}$ é o vetor de deslocamentos nodais; e $\mathbf{f}(t)$ é o vetor de forças externas.

**Matriz de Massa** — Diagonal, com cada entrada correspondendo à massa de um andar:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{M} = \begin{bmatrix} m_1 & 0 & 0 & 0 \\ 0 & m_2 & 0 & 0 \\ 0 & 0 & m_3 & 0 \\ 0 & 0 & 0 & m_4 \end{bmatrix} \tag{2.2}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

**Matriz de Rigidez** — Montada por assembleagem de elementos locais, inspirada no Método dos Elementos Finitos. Cada mola $k_i$ que conecta os nós $i{-}1$ e $i$ contribui com uma matriz local $2 \times 2$:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{K}^{(i)}_{\text{local}} = \begin{bmatrix} k_i & -k_i \\ -k_i & k_i \end{bmatrix} \tag{2.3}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Após a assembleagem global e a aplicação da condição de contorno de base fixa, a matriz de rigidez assume a forma **tridiagonal** típica do shear building:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{K} = \begin{bmatrix} k_1+k_2 & -k_2 & 0 & 0 \\ -k_2 & k_2+k_3 & -k_3 & 0 \\ 0 & -k_3 & k_3+k_4 & -k_4 \\ 0 & 0 & -k_4 & k_4 \end{bmatrix} \tag{2.4}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

A diagonal principal representa a rigidez de restauração de cada andar (soma das molas adjacentes). As superdiagonais e subdiagonais representam o acoplamento entre andares consecutivos — reflexo direto do fato de que cada andar interage apenas com seus vizinhos imediatos.

Neste trabalho considera-se o sistema **não amortecido**: $\mathbf{C} = \mathbf{0}$.

---

### 2.3 Formulação em Espaço de Estados

Para generalizar a análise ao caso com amortecimento arbitrário, reformula-se o sistema de segunda ordem (Eq. 2.1) como um sistema de primeira ordem equivalente. Define-se o **vetor de estado**:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{z} = \begin{Bmatrix} \mathbf{x} \\ \dot{\mathbf{x}} \end{Bmatrix} \tag{2.5}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

de modo que a equação de movimento se torna:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\dot{\mathbf{z}} = \mathbf{Q}\,\mathbf{z} \tag{2.6}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

onde $\mathbf{Q}$ é a **matriz de estado** de dimensão $2n \times 2n$:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{Q} = \begin{bmatrix} \mathbf{0} & \mathbf{I} \\ -\mathbf{M}^{-1}\mathbf{K} & -\mathbf{M}^{-1}\mathbf{C} \end{bmatrix} \tag{2.7}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Para o sistema sem amortecimento ($\mathbf{C} = \mathbf{0}$):

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{Q} = \begin{bmatrix} \mathbf{0} & \mathbf{I} \\ -\mathbf{M}^{-1}\mathbf{K} & \mathbf{0} \end{bmatrix} \tag{2.8}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Para o sistema de 4 graus de liberdade estudado, $\mathbf{Q}$ tem dimensão $8 \times 8$.

---

### 2.4 Análise de Autovalores

Os parâmetros modais são obtidos pelo problema de autovalores:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{Q}\,\boldsymbol{\psi}_r = \lambda_r\,\boldsymbol{\psi}_r \tag{2.9}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

Para o sistema não amortecido, os autovalores ocorrem em pares **puramente imaginários conjugados**:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\lambda_r = \pm\, i\,\omega_r \tag{2.10}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

onde $\omega_r = |\lambda_r|$ é a **frequência natural** (rad/s) do $r$-ésimo modo. No plano complexo, esses autovalores se distribuem sobre o eixo imaginário, sem parte real — consequência direta da ausência de dissipação de energia no sistema.

Para o caso amortecido, os autovalores passariam a ter **parte real negativa**:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\lambda_r = -\zeta_r\omega_r \pm i\,\omega_r\sqrt{1-\zeta_r^2} \tag{2.11}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

permitindo extrair diretamente tanto a frequência natural amortecida quanto a razão de amortecimento $\zeta_r$.

Os **autovetores** $\boldsymbol{\psi}_r$ descrevem as **formas modais**: o padrão relativo de deslocamentos de cada andar durante a vibração no modo $r$. No modo fundamental, todos os andares se movem na mesma direção com amplitudes crescentes da base ao topo. Nos modos superiores, surgem **nós de vibração** — posições de deslocamento nulo — com inversão de fase entre andares consecutivos.

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║   3. IMPLEMENTAÇÃO COMPUTACIONAL ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 3 Implementação Computacional

A implementação foi desenvolvida em Python utilizando a biblioteca NumPy para operações matriciais e o módulo `numpy.linalg` para a solução do problema de autovalores. O fluxo de implementação segue diretamente as etapas da Metodologia:

1. Definição dos parâmetros do sistema ($m_i$, $k_i$);
2. Montagem da matriz de massa $\mathbf{M}$ diagonal;
3. Montagem da matriz de rigidez $\mathbf{K}$ por assembleagem elemento a elemento, usando o vetor de **conectividade** para mapear cada mola na estrutura global;
4. Aplicação da condição de contorno de base fixa (eliminação da linha e coluna do nó 0);
5. Construção da matriz de estado $\mathbf{Q}$ em blocos;
6. Extração dos autovalores e autovetores via `numpy.linalg.eig`.

A abordagem de assembleagem por conectividade, inspirada no MEF, torna o código **parametrizado e generalizável**: a simples alteração do vetor de massas, rigidezes e conectividade permite analisar estruturas com qualquer número de andares ou topologia.

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         4. RESULTADOS            ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 4 Resultados

Para o caso base com todos os parâmetros unitários ($m_i = 1\,\text{kg}$, $k_i = 1\,\text{N/m}$), a matriz de rigidez global resultante após a aplicação das condições de contorno é:

</div>

<br>

<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; margin: 16px 0;">

$$\mathbf{K} = \begin{bmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 1 \end{bmatrix} \tag{4.1}$$

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

A decomposição em autovalores da matriz de estado $\mathbf{Q}$ ($8 \times 8$) retorna 8 autovalores distribuídos em 4 pares complexos conjugados puramente imaginários, conforme esperado para um sistema não amortecido. Os autovalores obtidos foram:

</div>

<br>

<!-- Tabela de autovalores -->
<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin: 20px 0;">

**Tabela 1: Autovalores da Matriz de Estado $\mathbf{Q}$**

| Par | $\lambda_r$ |
|:---:|:---:|
| 1 | $\pm\, 0{,}3473\,i$ |
| 2 | $\pm\, 1{,}0000\,i$ |
| 3 | $\pm\, 1{,}5321\,i$ |
| 4 | $\pm\, 1{,}8794\,i$ |

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

A ausência de parte real confirma que o sistema é conservativo. As frequências naturais, períodos e formas modais normalizadas são apresentados na Tabela 2.

</div>

<br>

<!-- Tabela de frequências -->
<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin: 20px 0;">

**Tabela 2: Parâmetros Modais — Shear Building 4 andares ($m_i = k_i = 1$)**

| Modo | $\omega_r$ [rad/s] | $f_r$ [Hz] | $T_r$ [s] |
|:---:|:---:|:---:|:---:|
| 1 | 0,3473 | 0,0553 | 18,09 |
| 2 | 1,0000 | 0,1592 | 6,28 |
| 3 | 1,5321 | 0,2438 | 4,10 |
| 4 | 1,8794 | 0,2991 | 3,34 |

</div>

<br>

<!-- Tabela de formas modais -->
<div align="center" style="font-family: 'Times New Roman', Times, serif; font-size: 11pt; margin: 20px 0;">

**Tabela 3: Formas Modais Normalizadas — Componentes de deslocamento por andar**

| Andar | Modo 1 | Modo 2 | Modo 3 | Modo 4 |
|:---:|:---:|:---:|:---:|:---:|
| 1 | −0,1551 | −0,1558 |  0,3681 | −0,3473 |
| 2 | −0,1316 | −1,0000 | −0,6605 | −0,6527 |
| 3 | −0,6701 |  0,0278 |  0,4241 | −0,8794 |
| 4 |  1,0000 |  0,9658 |  1,0000 | −1,0000 |

</div>

<br>

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

As formas modais normalizadas e os autovalores no plano complexo são apresentados graficamente nas Figuras 1 e 2, respectivamente.

**Figura 1** — As formas modais revelam o comportamento físico de cada modo. O **Modo 1** (fundamental) apresenta todos os andares se deslocando na mesma direção, com amplitudes crescendo monotonicamente da base ao topo — comportamento típico sob excitação sísmica de base. O **Modo 2** apresenta um nó entre os andares 2 e 3. Os **Modos 3 e 4** exibem padrões de inversão de fase progressivamente mais complexos, com amplitudes menores nos andares intermediários.

**Figura 2** — No plano complexo, todos os 8 autovalores se posicionam sobre o eixo imaginário puro, distribuídos simetricamente em relação à origem. Isso é a assinatura geométrica de um sistema **hamiltoniano conservativo**: ausência total de dissipação de energia, e portanto ausência de decaimento da resposta livre.

</div>

<br>

<div align="center">

![Formas Modais](/src/fig1_modos.png)

**Figura 1:** Formas modais normalizadas do shear building de 4 andares.

</div>

<br>

<div align="center">

![Autovalores no Plano Complexo](/src/fig2_autovalores.png)

**Figura 2:** Distribuição dos autovalores da matriz de estado $\mathbf{Q}$ no plano complexo.

</div>

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         5. CONCLUSÃO             ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 5 Conclusão

O presente trabalho apresentou a formulação teórica e a implementação computacional da análise modal de um shear building de 4 andares por meio da formulação em espaço de estados. A abordagem adotada permite obter, de forma direta e sistemática, as frequências naturais e as formas modais do sistema pela decomposição em autovalores da matriz de estado $\mathbf{Q}$.

A montagem das matrizes por assembleagem de elementos locais, inspirada no MEF, confere ao código uma estrutura parametrizada e extensível para estruturas com número arbitrário de andares ou parâmetros não uniformes. A formulação em espaço de estados, por sua vez, é diretamente aplicável ao caso com amortecimento geral — sem a hipótese de proporcionalidade —, bastando fornecer a matriz $\mathbf{C}$ adequada para que os autovalores passem a apresentar parte real negativa, permitindo a extração das razões de amortecimento modais $\zeta_r$.

Os resultados numéricos obtidos para o caso base unitário são consistentes com os valores analíticos esperados para o problema, com 4 pares de autovalores puramente imaginários posicionados sobre o eixo imaginário do plano complexo, confirmando o caráter conservativo do sistema modelado. Como perspectivas de continuidade, propõe-se a extensão do modelo para incluir amortecimento de Rayleigh, excitação harmônica e sísmica de base, e a comparação dos resultados com simulações em ambiente Simcenter Femap.

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║          6. APÊNDICE             ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 6 Apêndice

### 6.1 Código — Python

```python
import numpy as np
from numpy.linalg import inv, eig

## DEFINIÇÕES
m1, m2, m3, m4 = 1, 1, 1, 1
k1, k2, k3, k4 = 1, 1, 1, 1

## VETOR DE MASSAS E NÚMERO DE GRAUS DE LIBERDADE
m_n = np.array([m1, m2, m3, m4])
n_massas = len(m_n)

## MATRIZES AUXILIARES
Z = np.zeros([n_massas, n_massas])
I = np.identity(n_massas)

## MATRIZ DE MASSA
M = np.diag(m_n)

## MATRIZ DE AMORTECIMENTO (sistema não amortecido)
C = Z

## CONECTIVIDADE — [nó_i, nó_j] de cada mola
conectividade = np.array([[0, 1],
                          [1, 2],
                          [2, 3],
                          [3, 4]])

k_n = np.array([k1, k2, k3, k4])

## MONTAGEM DA MATRIZ DE RIGIDEZ GLOBAL (n+1 x n+1)
K = np.zeros([n_massas + 1, n_massas + 1])

for k, elemento in zip(k_n, conectividade):
    k_local = np.array([[ k, -k],
                        [-k,  k]])
    K[np.ix_(elemento, elemento)] += k_local

## APLICAÇÃO DAS CONDIÇÕES DE CONTORNO (base fixa — nó 0)
total_dof = np.arange(0, n_massas + 1, 1)
free_dof  = total_dof[1:]
K = K[np.ix_(free_dof, free_dof)]

## MATRIZ DE ESTADO Q (2n x 2n)
Q = np.block([[Z,           I          ],
              [-inv(M) @ K, -inv(M) @ C]])

## SOLUÇÃO DO PROBLEMA DE AUTOVALORES
autovalores, autovetores = eig(Q)

## EXTRAÇÃO DAS FREQUÊNCIAS NATURAIS
omega = np.sort(np.unique(np.round(np.abs(autovalores.imag), 6)))
omega = omega[omega > 1e-10]

print("Frequências naturais (rad/s):", omega)
print("Frequências naturais (Hz):   ", omega / (2 * np.pi))
print("Períodos (s):                ", (2 * np.pi) / omega)
```

</div>

---

<!-- ╔══════════════════════════════════╗ -->
<!-- ║         7. REFERÊNCIAS           ║ -->
<!-- ╚══════════════════════════════════╝ -->

<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt; text-align: justify; line-height: 1.5;">

## 7 Referências

CHOPRA, A. K. *Dynamics of Structures: Theory and Applications to Earthquake Engineering*. 5. ed. Hoboken: Pearson, 2017.

CLOUGH, R. W.; PENZIEN, J. *Dynamics of Structures*. 3. ed. Berkeley: Computers & Structures, 2003.

EWINS, D. J. *Modal Testing: Theory, Practice and Application*. 2. ed. Baldock: Research Studies Press, 2000.

INMAN, D. J. *Engineering Vibration*. 4. ed. Upper Saddle River: Pearson, 2014.

</div>