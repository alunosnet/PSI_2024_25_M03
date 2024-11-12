def Soma():
    """
    A função soma os valores 10 e 5 e mostra o resultado
    """
    print(10+5)

def Soma2(x,y):
    """
    A função recebe dois números e soma os dois para dar o resultado

    x,y: dois valores numéricos
    Exemplo:
    Soma2(10,5)
    """
    print(x+y)
    
def main():
    Soma()
    Soma2(30,40)
    Soma2(-5,80)

if __name__=="__main__":
    main()