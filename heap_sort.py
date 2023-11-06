"""
1) Passo
    1 2 3 4 5 6 7 8 índices
    1 0 2 6 3 4 7 5 valores
    2 0 1
    2 6 1 0
    6 2 1 0
    6 3 1 0 2
    6 3 4 0 2 1
    6 3 7 0 2 1 4
    7 3 6 0 2 1 4 
    7 3 6 5 2 1 4 0
    7 5 6 3 2 1 4 0
2) Passo
    1 2 3 4 5 6 7 8 índices
    7 5 6 3 2 1 4 0 troca 7 por 0 (primeiro pelo último)
    0 5 6 3 2 1 4 7 
    6 5 0 3 2 1 4  
    6 5 4 3 2 1 0 troca 6 por 0
    0 5 4 3 2 1 6 
    5 0 4 3 2 1
    5 3 4 0 2 1 troca 5 por 1
    1 3 4 0 2 5
    4 3 1 0 2 troca 4 por 2
    2 3 1 0 4
    3 2 1 0  troco 3 por 0
    0 2 1 3
    2 0 1 troco 2 por 1
    1 0 2 troco 1 por 0
    0 1
    0 1 2 3 4 5 6 7  n * log(n, 2)
    
    2 * log(n, 2) * n
"""