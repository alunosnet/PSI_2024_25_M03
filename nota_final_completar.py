def NotaValida(nota):
    if nota<0 or nota>20:
        return False
    return True

#Completa a função de acordo com a docstring
def NotaFinal():
    """
    Recebe 3 números inteiros entre 0 e 20 e calcula a nota final sabendo que a primeira nota (dominio 1) tem um peso de 30%, a segunda nota (dominio 2) tem um peso de 40% e a terceira nota (dominio 3) tem um peso de 30%
    Parâmetros:
        nota1, nota2, nota3: números inteiros entre 0 e 20
    Devolve:
        inteiro com a nota final do aluno
        None se alguma das notas não é válida
    """
    pass

#Testes
assert NotaFinal(10,10,10) == 10, "Erro a função devia devolver 10"
assert NotaFinal(15,10,5) == 10, "Erro a função devia devolver 10"
assert NotaFinal(10,18,21) == None,"Erro a função devia devolver None"
assert NotaFinal(15,5,10) == 10, "Erro a função devia devolver 10"
assert NotaFinal(-10,18,10) == None,"Erro a função devia devolver None"
assert NotaFinal(10,21,11) == None,"Erro a função devia devolver None"

print("Função passou nos testes")