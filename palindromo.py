def Palindromo(palavra) ->bool:
    """
    Função que indica se uma palavra é um palindromo.
    Parâmetros:
        palavra: string a testar
    Devolve:
        True: se é palindromo
        False: se não é palindrom
    """
    #converter a palavra para minusculas
    palavra = palavra.lower()
    palavra_invertida=""
    for posicao in range(len(palavra)-1,-1,-1):
        palavra_invertida = palavra_invertida + palavra[posicao]
        
    if palavra == palavra_invertida:
        return True
    return False

if Palindromo("banana") == True:
    print("Banana é um palindromo")
else:
    print("Banana não é palindromo")

if Palindromo("anana") == True:
    print("Anana é um palindromo")
else:
    print("Anana não é palindromo")