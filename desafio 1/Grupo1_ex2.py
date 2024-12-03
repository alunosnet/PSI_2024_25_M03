"""
2.	Crie uma função que mostra a média de 5 valores. A função deve ler os valores do utilizador e, posteriormente, calcular e mostrar a média dos valores.
"""
def Media():
    n1 = int(input("Introduza um nº:"))
    n2 = int(input("Introduza um nº:"))
    n3 = int(input("Introduza um nº:"))
    n4 = int(input("Introduza um nº:"))
    n5 = int(input("Introduza um nº:"))
    soma = n1 + n2 + n3 + n4 + n5
    media = soma / 5
    print(media)

def Media_v2():
    soma = 0
    for _ in range(5):
        n = int(input("Introduza um nº:"))
        soma = soma + n
    media = soma / 5
    print(media)