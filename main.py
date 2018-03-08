import numpy as np
import math
from utils import somme
import pandas as pd




la=1000
x0=10**6
m=10**3
matrix_t_sinistre=[]
nombre_trajectoires=1
cc=la*m
c=cc

#calcul des t_sinistre
for i in range(0,nombre_trajectoires):
    t_sinistre=0
    liste_t_sinistre=[0]

    while(t_sinistre<1):
        t_plus_un=t_sinistre - (1 / la) * math.log(np.random.uniform(0, 1))
        liste_t_sinistre.append(t_plus_un)
        t_sinistre=t_plus_un

    matrix_t_sinistre.append(liste_t_sinistre)

print(matrix_t_sinistre)

matrix_yk=[]

#calcul des yk

for liste_t_sinistre in matrix_t_sinistre:

    yk=[0]
    for t_sinistre in liste_t_sinistre[1:]:

        yk.append(np.random.exponential(m))
    matrix_yk.append(yk)


#calcul de la matrix des Xt

matrix_xt=[]
for i in range(0,nombre_trajectoires):
    print(i)
    xt=[]
    t=0;
    while(t<1):

        xt.append(x0+c*t-somme(t,matrix_t_sinistre[i],matrix_yk[i]))

        t+=0.001

    matrix_xt.append(xt)


my_df = pd.DataFrame(matrix_xt)
print(len(matrix_xt[0]))
my_df.to_csv('out.csv', index=False, header=False)


