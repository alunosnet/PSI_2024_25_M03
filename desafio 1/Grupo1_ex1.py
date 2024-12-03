"""
Crie uma função que recebe dois parâmetros. A função deve calcular e mostrar a soma de todos os números inteiros entre os dois parâmetros, inclusive.
"""
def Somar(x1,x2):
    soma = 0
    for x in range(x1,x2+1):
        soma = soma + x
    print(soma)