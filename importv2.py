#Programa para ler as notas de 3 alunos e calcular a média
from funcoes_media import MediaD

nota1 = int(input("Introduza uma nota: "))
nota2 = int(input("Introduza uma nota: "))
nota3 = int(input("Introduza uma nota: "))

media = MediaD(nota1,nota2,nota3)

print(f"A média das notas é de {media}")