"""Exemplos de funções recursivas, quando ocorre a chamada recursiva diminui-se a instância.
    Nem toda função recursiva é eficiente, pois pode haver muitas chamadas recursivas.
    Exemplo: Fibonacci(100) repete coisas calculadas anteriormente.
"""
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    print(f'fib({n})')
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)


def fat(n):
    if n <=1: return 1
    return n * fat(n-1)


def pot (x, n):
    if n==0: return 1
    return x * pot(x, n-1)


def inv(s):
    if len(s) <= 1: return s
    return inv(s[1:]) + s[0]


def mdc(a, b):
    if a % b == 0: return b
    return mdc(b, a % b)


if __name__ == '__main__':
    print(fib(9))