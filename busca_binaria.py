
def busca_binaria(elemento, lista):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1
    
    return -1


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 10, 11, 22, 33, 423, 234325]
    print(busca_binaria(2, lista))