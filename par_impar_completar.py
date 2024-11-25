#Completa a função de acordo com a docstring
def Par():
    """
    Recebe um nº inteiro positivo e calcula se é par
    Parâmetro:
        n: nº inteiro positivo
    Devolve:
        True se n é par
        False se n não é par
    """
    pass

#Testes
assert Par(2) == True, "Erro a função devia devolver True"
assert Par(3) == False, "Erro a função devia devolver False"

for i in range(1,20,2):
    assert Par(i) == False, f"Erro a função não devolveu false para o valor {i}"

print("Função passou nos testes")