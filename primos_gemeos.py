"""
Dois números primos gémeos são dois nº primos que distam em 2 unidades um do outro
p.ex:
    3 e 5
    5 e 7
Fazer um programa que lê dois nº inteiros positivos do utilizador e diz se são primos e primos gémeos
"""
import primo
from utils import ler_numero_inteiro

#ler dois nº inteiros positivos
n1 = ler_numero_inteiro("Introduza um nº inteiro: ")
n2 = ler_numero_inteiro("Introduza outro nº inteiro: ")

#testar se são primos
if primo.Primo(n1) and primo.Primo(n2):
    #calcular a diferença
    diferenca = n1 - n2
    if abs(diferenca) == 2:
        print(f"Os valores {n1} e {n2} são primos gémeos")
    else:
        print(f"Os valores {n1} e {n2} são primos")
else:
    if primo.Primo(n1):
        print(f"O valor {n1} é primo")
    elif primo.Primo(n2):
        print(f"O valor {n2} é primo")
    else:
        print("Nenhum dos valores é primo")
