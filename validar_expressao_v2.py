"""
Programa para validar uma expressão matemática quanto aos () e []
"""
#Pedir a expressão ao utilizador
expressao = input("Introduza uma expressão matemática:")
#fazer a validação com uma função
def Validar(expressao):
    """
    Função que recebe uma expressão matemática para validade os ()
    A função devolve False se a expressão tiver erros de outra forma devolve True
    """
    abriu = ""
    for l in expressao:
        if l == '(' or l == '[':
            abriu = abriu + l
        if l == ')' or l == ']':
            if abriu == "":
                return False
            ultimo = abriu[len(abriu)-1]
            if (ultimo == '(' and l ==')') or (ultimo=='[' and l ==']'):
                temp = abriu
                #limpar a string para copiar todos os carateres menos o último
                abriu = ""
                for i in range(len(temp)-1):
                    abriu = abriu + temp[i] 
            else:
                return False
    if abriu == "":
        return True
    return False

#Chamar a função
resultado = Validar(expressao)

#indicar ao utilizador se a expressão é ou não válida
if resultado == False:
    print("A expressão não é válida")
else:
    print("A expressão válida")