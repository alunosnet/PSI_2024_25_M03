#Completa a função de acordo com a docstring
def RepetidasSeguidas(texto):
    """
    Recebe uma string com um texto que deve ser verificado para encontrar letras seguidas iguais
    Parâmetro:
        texto: string a verificar
    Devolve:
        True: se o texto contém letras seguidas iguais
        False: se o texto não tem letras seguidas iguais
    """
    texto = texto.lower()
    for i in range(len(texto)-1):
        if texto[i]==texto[i+1]:
            return True
    return False

assert RepetidasSeguidas("Ana") == False, "Erro a função devia devolver False"
assert RepetidasSeguidas("Assar") == True, "Erro a função devia devolver True"
assert RepetidasSeguidas("") == False,"Erro a função devia devolver False"
assert RepetidasSeguidas("AsSado") == True, "Erro a função devia devolver False"

print("Função passou nos testes")