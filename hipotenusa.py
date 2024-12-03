"""
Escreva uma função que, receba como parâmetros de entrada as medidas dos dois catetos de um triângulo retângulo, e devolva a medida da hipotenusa com 3 casa decimais.
"""
import math

def Hipotenusa(c1:float,c2:float) -> float:
    # h^2 = c1^2 + c2^2
    # h = sqrt(c1^2 + c2^2)
    h = math.sqrt(c1 ** 2+c2**2)
    return h

assert Hipotenusa(4,3)==5, "Função devolveu o valor errado, devia dar 5"
print("Função passou nos testes")