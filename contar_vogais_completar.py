#Completa a função de acordo com a docstring
def ContaVogais():
    """
    Recebe uma string e conta o nº de vogais
    Parâmetro:
        texto - string para contar as vogais
    Devolve:
        nº de vogais
    """
    pass

#Testes
assert ContaVogais("Ana") == 2, "Erro a função devia devolver 2"
assert ContaVogais("ZZZ") == 0, "Erro a função devia devolver 0"

print("Função passou nos testes")