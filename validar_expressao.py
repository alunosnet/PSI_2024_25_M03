"""
Programa para validar uma expressão matemática quanto aos ()
"""
#Pedir a expressão ao utilizador
expressao = input("Introduza uma expressão matemática:")
#fazer a validação com uma função
def Validar(expressao):
    """
    Função que recebe uma expressão matemática para validade os ()
    A função devolve False se a expressão tiver erros de outra forma devolve True
    """
    contar = 0
    for l in expressao:
        if l == '(':
            contar = contar + 1
        if l == ')':
            contar = contar - 1
        if contar < 0:
            return False
    if contar == 0:
        return True
    return False

#Chamar a função
resultado = Validar(expressao)

#indicar ao utilizador se a expressão é ou não válida
if resultado == False:
    print("A expressão não é válida")
else:
    print("A expressão válida")