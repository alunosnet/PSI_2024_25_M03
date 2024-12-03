"""
1.	Desenvolva uma função que recebe uma string e devolve verdadeiro se todas as letras da string são iguais e falso nos restantes casos.
"""
def LetrasIguais(texto):
    for letra in texto:
        if letra != texto[0]:
            return False
    return True