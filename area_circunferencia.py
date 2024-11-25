import math
#Completa a função de acordo com a docstring
def Area(raio):
    """
    Recebe o raio e calcula a área de uma circunferencia utilizando a fórmula A = PI * Raio ** 2
    
    O valor de pi pode ser obtido assim math.pi
    
    Parâmetro:
        raio: valor real maior do que zero
    Devolve:
        valor real com duas casas decimais
        None se o valor do raio não é válido
    """
    if raio <= 0:
        return None
    area = math.pi * raio ** 2

    return round(area,2)

assert Area(1) == 3.14, "Erro a função devia devolver 3.14"
assert Area(-1) == None, "Erro a função devia devolver None"
assert Area(10) == 314.16, "Erro a função devia devolver 314.16"
print("Função passou nos testes")