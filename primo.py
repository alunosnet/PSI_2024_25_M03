def Primo(n) -> bool:
    """
    Função que indica se um nº é primo
    Parametros:
        n: nº inteiro positivo
    Devolve:
        True se nº é primo
        False se º não é primo
    """
    E_Primo = True
    for i in range(2,n):
        if n % i == 0:
            E_Primo=False
            break
    return E_Primo

# if Primo(5) == True:
#     print("O nº 5 é primo")
# else:
#     print("O nº 5 não é primo")

# if Primo(10) == True:
#     print("O nº 10 é primo")
# else:
#     print("O nº 10 não é primo")