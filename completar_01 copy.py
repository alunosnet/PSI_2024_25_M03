"""Completa as seguintes funções"""

def E_Impar(numero:int) -> bool:
    """Devolve true se o numero é impar e false se par"""
    if numero % 2 == 0:
        return False
    return True

print("Testes E_Impar")
assert E_Impar(10) == False, "Erro no primeiro teste. Devia dar False"
assert E_Impar(11) == True, "Erro no segundo teste. Devia dar True"
print("Completou testes E_Impar")

############################################################################
def Ola_User(nome:str):
    """Diz olá ao user. Se nome não estiver preenchido não diz nada"""
    if nome=="":
        return
    print(f"Olá {nome}")

print("Testes Ola_User")
Ola_User("")        #Com este argumento não deve mostrar nada
Ola_User("Joaquim") #Com este argumento deve mostrar Olá Joaquim
print("Completou testes Ola_User")

#############################################################################
def JuntaDoisNomes(nome1:str,nome2:str) -> str:
    """Devolve os nomes numa string separados por um espaço em branco. O primeiro nome deve ser o que alfabeticamente for menor."""
    if nome1<nome2:
        return f"{nome1} {nome2}"
    return f"{nome2} {nome1}"

print("Testes JuntaDoisNomes")
assert JuntaDoisNomes("Joaquim","Ana") == "Ana Joaquim", "Erro no quinto teste, devia dar Ana Joaquim"
assert JuntaDoisNomes("Maria","Zé") == "Maria Zé","Erro no sexto teste, devia dar Maria Zé"
print("Completou testes JuntaDoisNomes")

#############################################################################
maior = ""

def QualOMaior(nome1:str, nome2: str):
    """Função para alterar a variável global maior e guarda o nome com mais letras. Caso sejam de igual tamanho deve guardar a palavra Iguais"""
    global maior
    if len(nome1) > len(nome2):
        maior = nome1
    elif len(nome2) > len(nome1):
        maior = nome2
    else:
        maior = "Iguais"


print("Testes QualOMaior")
QualOMaior("Ana","Maria")
assert maior == "Maria", "Erro no sétimo teste, maior devia ser Maria"
QualOMaior("João","José")
assert maior == "Iguais", "Erro no oitavo teste, maior devia ser Iguais"
QualOMaior("António","Zé")
assert maior == "António", "Erro no nono teste, maior devia ser António"
print("Completou testes QualOMaior")
