"""
Implemente um programa que condifica ou descodifica uma mensagem com base nos alfabetos fornecidos.
"""
original = "abcdefghijklmnopqrstuvwxyz"
codigo   = "bcdefghijklmnopqrstuvwxyza"

def menu():
    """Função para ler a opção do utilizador e executar a função adequada: codificar ou descodificar"""
    print(codifica("olá mundo"))

def codifica(mensagem:str)->str:
    """
    Função que recebe uma mensagem e devolve a mesma codificada de acordo com os alfabetos fornecidos
    """
    global original
    global codigo
    texto = ""
    mensagem = mensagem.lower()
    for l in mensagem:
        #caso não encontre a letra no alfabeto deve manter a letra original
        if l not in original:
            texto = texto + l
        else:
            for p in range(len(original)):
                if l == original[p]:
                    texto = texto + codigo[p]
    return texto

def descodifica(mensagem_codificada:str)->str:
    """
    Função que recebe uma mensagem codificada e devolve a mesma descodificada de acordo com os alfabetos fornecidos
    """
    global original
    global codigo
    texto = ""
    mensagem = mensagem.lower()
    for l in mensagem:
        #caso não encontre a letra no alfabeto deve manter a letra original
        if l not in codigo:
            texto = texto + l
        else:
            for p in range(len(codigo)):
                if l == codigo[p]:
                    texto = texto + original[p]
    return texto

def main():
    menu()

if __name__=='__main__':
    main()