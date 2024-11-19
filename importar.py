#Programa para ler as notas de 3 alunos e calcular a média
import funcoes_media

nota1 = int(input("Introduza uma nota: "))
nota2 = int(input("Introduza uma nota: "))
nota3 = int(input("Introduza uma nota: "))

media = funcoes_media.MediaD(nota1,nota2,nota3)

print(f"A média das notas é de {media}")