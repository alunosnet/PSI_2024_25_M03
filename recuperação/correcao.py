def Mostrar_Criterios():
    print("""Domínio Resolver Problemas e Criar Conteúdos: 40%\n
    Domínio Conhecimento Científico: 30%\n
    Domínio Comunicar e Colaborar: 30%\n
    """)

def Calcular_Nota(d1,d2,d3):
    nota_final = d1*0.4 + d2*0.3 + d3*0.3
    nota_arred = round(nota_final,0)
    return nota_arred

def Atribuir_Classificacao(nota):
    if nota < 10:
        return "Reprovado"
    elif nota >= 10 and nota<=14:
        return "Suficiente"
    elif nota>=15 and nota<=18:
        return "Bom"
    else:
        return "Muito Bom"

Mostrar_Criterios()
n1 = int(input("Nota do dominio 1: "))
n2 = int(input("Nota do dominio 2: "))
n3 = int(input("Nota do dominio 3: "))
#validação
if (n1 >=0 and n1 <=20) and (n2 >=0 and n2 <=20) and (n3 >=0 and n3 <=20):
    nota = Calcular_Nota(n1,n2,n3)
    print("Nota:",nota)
    print(Atribuir_Classificacao(nota))
else:
    print("Erro! As notas introduzidas devem estar entre 0 e 20.")