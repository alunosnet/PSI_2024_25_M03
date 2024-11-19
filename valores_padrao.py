def Saudacao(texto="Mundo"):
    print(f"Olá, {texto}")

def Saudacao2(nome, parte_dia="Bom dia"):
    print(f"{parte_dia}, {nome}")

#Saudacao()
#Saudacao("Joaquim")
Saudacao2(parte_dia="Bom dia",nome="Joaquim")
Saudacao2("Boa tarde","Maria")
Saudacao2(nome="Joaquim")