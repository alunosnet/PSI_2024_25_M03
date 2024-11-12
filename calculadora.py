"""
Programa para implementar uma calculadora simples utilizando funções
"""
def menu():
    """
    Mostra ao utilizador as operações que a calculadora vai realizar
    """
    print("1.Somar\n2.Subtrair\n3.Multiplicar\n4.Dividir")
    op = input()
    
def main():
    menu()

if __name__ == "__main__":
    main()