% 1. Definição dos parâmetros
m1 = 1; m2 = 1; m3 = 1; m4 = 1;
k1 = 1; k2 = 1; k3 = 1; k4 = 1;

m_n = [m1, m2, m3, m4];
n_massas = length(m_n);
Z = zeros(n_massas, n_massas);
C = Z;

M = diag(m_n);

% 2. Montagem da matriz de rigidez global (K) pelo método de conectividade
% (Lembrando que o MATLAB começa no índice 1)
conectividade = [1, 2;
                 2, 3;
                 3, 4;
                 4, 5];

k_n = [k1, k2, k3, k4];
K = zeros(n_massas + 1, n_massas + 1);

for i = 1:length(k_n)
    k = k_n(i);
    elemento = conectividade(i, :);
    
    k_local = [k, -k;
              -k,  k];
    
    K(elemento, elemento) = K(elemento, elemento) + k_local;
end

% Condições de contorno (Corta o primeiro grau de liberdade)
total_dof = 1:(n_massas + 1);
free_dof = total_dof(2:end); 
K = K(free_dof, free_dof);

% 3. Montagem do Espaço de Estados (Q)
I = eye(n_massas);

% Usamos M\K e M\C que é a forma nativa e mais rápida do MATLAB para inv(M)*K
Q = [Z, I;
    -M\K, -M\C]; 

% 4. Resumo Automático com damp()
disp('--- Resumo Dinâmico do Sistema ---');
% Chamar damp(Q) sem atribuir a uma variável faz o MATLAB imprimir uma 
% tabela linda com Autovalor, Damping e Frequência Natural (rad/s)
damp(Q); 

% 5. Extração dos Modos de Vibração (Autovetores)
% O damp() não devolve os modos (autovetores), então usamos o eig() para isso
[autovetores, matriz_autovalores] = eig(Q);
autovalores = diag(matriz_autovalores);

% Filtro seguro para garantir que pegamos as colunas corretas dos modos
indices_validos = find(imag(autovalores) > 0);
[~, idx_sort] = sort(abs(autovalores(indices_validos)));
indices_ordenados = indices_validos(idx_sort);

w_n = abs(autovalores(indices_ordenados));
modo = abs(autovetores(1:n_massas, indices_ordenados));

disp('--- Formas Modais (Amplitudes) ---');
for i = 1:length(w_n)
    fprintf('Modo %d (%.4f rad/s):\n', i, w_n(i));
    disp(modo(:, i));
end