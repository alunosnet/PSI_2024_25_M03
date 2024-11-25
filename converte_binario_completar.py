#Completa a função de acordo com a docstring
def ConverteBinario():
    """
    Recebe um nº inteiro positivo de base 10 e calcula o valor convertido na base 2 (binário)
    Parâmetro:
        n: nº inteiro positivo
    Devolve:
        string com o valor em binário
    """
    pass

#Testes
assert ConverteBinario(2) == "10", "Erro a função devia devolver 10"
assert ConverteBinario(1) == "1", "Erro a função devia devolver 1"
assert ConverteBinario(3) == "11","Erro a função devia devolver 11"
assert ConverteBinario(0) == "0", "Erro a função devia devolver 0"

print("Função passou nos testes")