#Completa a função de acordo com a docstring
def ConverteBinario(n):
    """
    Recebe um nº inteiro positivo de base 10 e calcula o valor convertido na base 2 (binário)
    Parâmetro:
        n: nº inteiro positivo
    Devolve:
        string com o valor em binário
    """
    if n==0:
        return "0"
    resto = n % 2
    n = n // 2
    convertido = str(resto)
    while resto < n:
        resto = n % 2
        n = n // 2
        convertido = str(resto) + convertido
    if n!=0:
        convertido = str(n) + convertido
    print(convertido)
    return convertido

assert ConverteBinario(2) == "10", "Erro a função devia devolver 10"
assert ConverteBinario(1) == "1", "Erro a função devia devolver 1"
assert ConverteBinario(3) == "11","Erro a função devia devolver 11"
assert ConverteBinario(0) == "0", "Erro a função devia devolver 0"

print("Função passou nos testes")