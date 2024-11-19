"""a)Uma função que calcula a média de 3 números inteiros.
A função deve ler do utilizador os 3 números, calcular e mostrar a média.
"""
def MediaA() -> None:
    n1 = int(input("Introduza um nº: "))
    n2 = int(input("Introduza um nº: "))
    n3 = int(input("Introduza um nº: "))
    media = (n1 + n2 + n3) / 3
    print(f"A média é {media}")

"""
b)Uma função que calcula a média de 3 números inteiros.
A função deve RECEBER os 3 números, calcular e mostrar a média.
"""
def MediaB(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    print(f"A média é {media}")
    
"""
c)Uma função que calcula a média de 3 números inteiros.
A função deve ler do utilizador os 3 números, calcular e DEVOLVER a média.
"""
def MediaC():
    n1 = int(input("Introduza um nº: "))
    n2 = int(input("Introduza um nº: "))
    n3 = int(input("Introduza um nº: "))
    media = (n1 + n2 + n3) / 3
    return media    #devolve o valor da media

"""
d)Uma função que calcula a média de 3 números inteiros.
A função RECEBER os 3 números, calcular e DEVOLVER a média.
"""
def MediaD(n1,n2,n3) -> float:
    media = (n1+n2+n3) / 3
    return media

def main():
    #MediaA()
    #n1 = int(input("Introduza um nº "))
    #MediaB(5,5,5)
    #print(f"A média é {MediaC()}") #chama a função e mostra o valor devolvido
    print(f"A média é {MediaD(5,5,5)}") #chama a função com os argumentos e mostra o valor devolvido

if __name__ == '__main__':
    main()