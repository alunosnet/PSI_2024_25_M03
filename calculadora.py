"""
Programa para implementar uma calculadora simples utilizando funções
"""
def Somar(n1,n2):
    """Função que recebe dois nº e mostrar a sua soma"""
    print(n1 + n2)
    #menu() NUNCA FAZER ISTO
    
def Subtrair(n1,n2):
    """Função que recebe dois nº e mostrar a diferença"""
    print(n1 - n2)
def Multiplicar(n1,n2):
    """Função que recebe dois nº e mostrar o produto"""
    print(n1 * n2)
def Dividir(n1,n2):
    """Função que recebe dois nº e mostrar a divisão"""
    print(n1 / n2)

def menu():
    """
    Mostra ao utilizador as operações que a calculadora vai realizar
    """
    op='0'
    while op != '5':
        print("1.Somar\n2.Subtrair\n3.Multiplicar\n4.Dividir\n5.Terminar")
        op = input()

        if op=="5":
            break
        
        n1 = float(input("insira um nº: "))
        n2 = float(input("Insira um nº: "))
        
        if op =="1":
            Somar(n1,n2)
        elif op=="2":
            Subtrair(n1,n2)
        elif op=="3":
            Multiplicar(n1,n2)
        elif op=="4":
            Dividir(n1,n2)
        
def main():
    menu()

if __name__ == "__main__":
    main()