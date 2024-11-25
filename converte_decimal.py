#Completa a função de acordo com a docstring
def ConverteDecimal(n_binario):
    """
    Recebe uma string com o nº de base 2 (binário) e calcula o valor convertido na base 10 (decimal)
    Parâmetro:
        n_binario: string com o nº na base 2
    Devolve:
        nº inteiro na base 10
    """
    pos = len(n_binario)-1
    convertido = 0
    for n in n_binario:
        convertido = convertido + int(n) * 2 ** pos
        pos -= 1
    print(convertido)
    return convertido

assert ConverteDecimal("10") == 2, "Erro a função devia devolver 2"
assert ConverteDecimal("1") == 1, "Erro a função devia devolver 1"
assert ConverteDecimal("11") == 3,"Erro a função devia devolver 3"
assert ConverteDecimal("0") == 0, "Erro a função devia devolver 0"

print("Função passou nos testes")