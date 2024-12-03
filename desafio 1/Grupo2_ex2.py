"""
2.	Escreva uma função que recebe três valores e devolve o maior, caso sejam todos positivos, caso os valores sejam todos negativos deve devolver o menor. Nas restantes situações devolve None.
"""
def MaiorOuMenor(a,b,c):
    # qual o maior
    if a > b:
        maior = a
    else:
        maior = b
    if c > maior:
        maior = c
    # qual o menor
    if a < b:
        menor = a
    else:
        menor = b
    if c < menor:
        menor = c
    if a > 0 and b > 0 and c > 0:
        return maior
    if a < 0 and b < 0 and c < 0:
        return menor
    return None
    