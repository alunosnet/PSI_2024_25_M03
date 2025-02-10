def NumeroPerfeito(n) -> bool:
    """
    Função que devolve true se o nº é perfeito e false se não
    """
    soma = 0
    for i in range(1,n):
        if n % i == 0:
            soma = soma + i
    if soma == n:
        return True
    return False

def Main():
    numero = int(input("Nº:"))
    if NumeroPerfeito(numero)==True:
        print("Número perfeito")
    else:
        print("Número não perfeito")

if __name__=='__main__':
    Main()