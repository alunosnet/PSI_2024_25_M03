"""
Um programa para ler as coordenadas de um ponto P(x,y) e indicar o quadrante em que o ponto se encontra.
"""

# x = int(input("Introduza a coordenada x do ponto:"))
# y = int(input("Introduza a coordenada y do ponto: "))

def Quadrante(x,y):
    # testar se o ponto está em cima de algum eixo
    if x == 0 or y == 0:
        return "O ponto está sobre os eixos."
    else:
        if x > 0:
            if y > 0:
                return "1º Quadrante"
            else:
                return "4º Quadrante"
        else:
            if y > 0:
                return "2º Quadrante"
            else:
                return "3º Quadrante"

assert Quadrante(5,5) == "1º Quadrante","Erro: a função não deu 1º Quadrante"
assert Quadrante(-5,10) == "2º Quadrante","Erro: a função não deu 2º Quadrante"
assert Quadrante(-1,-1) == "3º Quadrante","Erro: a função não deu 3º Quadrante"
assert Quadrante(1,-3) == "4º Quadrante","Erro: a função não deu 4º Quadrante"
assert Quadrante(0,5) == "O ponto está sobre os eixos.","Erro: a função não deu sobre os eixos"

print("A função passou nos testes")
