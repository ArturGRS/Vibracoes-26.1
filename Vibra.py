from glm import inverse
import numpy as np
from numpy.linalg import inv,eig


m1 = 1
m2 = 1
m3 = 1
m4 = 1

k1 = 1
k2 = 1
k3 = 1
k4 = 1

m_n = np.array([m1,m2,m3,m4])
n_massas = len(m_n)
Z = np.zeros([n_massas,n_massas])
C = Z

M = np.diag(m_n)

conectividade = np.array([[0,1],
                         [1,2],
                         [2,3],
                         [3,4]])



k_n = np.array([k1,k2,k3,k4])

K = np.zeros([n_massas+1,n_massas+1])

for k , elemento in zip(k_n,conectividade):
    
    k_local = np.array([[k , -k],
                       [-k , k]])
    
    K[np.ix_(elemento,elemento)] += k_local

total_dof = np.arange(0,n_massas+1, 1)

free_dof = total_dof[1:]  

K = K[np.ix_(free_dof,free_dof)]

I = np.identity(n_massas)

Q = np.block([[Z , I],
             [-inv(M) @ K , -inv(M) @ C]])

autovalores, autovetores = eig(Q)

print(autovalores,autovetores)