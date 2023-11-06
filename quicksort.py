"""
O algoritmo de ordenação QuickSort é um método de ordenação 
eficiente que utiliza a estratégia de dividir para conquistar. 
A ideia básica por trás do QuickSort é escolher um elemento do vetor, 
chamado de "pivot," e reorganizar os elementos do vetor de forma que 
os elementos menores que o pivot fiquem à esquerda e os elementos 
maiores fiquem à direita. Em seguida, o algoritmo é recursivamente 
aplicado aos subvetores à esquerda e à direita do pivot até que todo 
o vetor esteja ordenado.
Ex: 1 como pivô
    1 0 2 6 3 4 7 5
    0 1 2 6 3 4 7 5
        2 6 3 4 7 5
          3 4 5 6 7

    0 1 2 3 4 5 6 7
"""

def quicksort(v):
    if len(v) <= 1:
        return v
    pivo = v[0]
    iguais = [x for x in v if x == pivo] 
    menores = [x for x in v if x < pivo]
    maiores = [x for x in v if x  > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)