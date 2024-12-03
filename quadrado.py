"""
Elabore um programa que determine o quadrado de um número inteiro n. O número n deve ser pedido ao utilizador e, através de uma função, devolver o seu quadrado.
"""

def Quadrado(n: int) -> int:
    return n ** 2

def main():
    n = int(input("Qual o nº: "))
    q = Quadrado(n)
    print(f"O quadrado de {n} é {q}")

if __name__=='__main__':
    main()