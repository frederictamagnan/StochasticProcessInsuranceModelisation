#calcul de la somme des Yk selon t et les tk


def somme(t,liste_t_sinistre,yk):

    sum_yk=0
    for k,t_sinistre in enumerate(liste_t_sinistre):
        if t<t_sinistre:
            break

    for i in range(0,k):
        sum_yk+=yk[i]

    return sum_yk