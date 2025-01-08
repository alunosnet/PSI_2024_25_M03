"""Uma função que recebe uma palavra e devolve a mesma palavra convertida na lingua dos P
Alguns exemplos:
    Casa  -> Capasapa
    Bola  -> Bopolapa
    Olá   -> Opolápá
    Muito -> Muipuitopo
"""

def E_Vogal(letra:str) -> bool:
    """Função que devolve true/false se letra é vogal/consoante"""
    vogais="aeiouáàãéèêíìóòúùõô"
    if letra.lower() in vogais:
        return True
    return False

def ConverteSilaba(silaba:str) -> str:
    """Função que recebe uma silaba e junta a mesma silaba na lingua dos P
    P.E.: Ca -> Capa
          Mui -> Muipui
          O   -> Opo
    """
    if E_Vogal(silaba[0]):
        silaba = silaba + "p" + silaba.lower()
    else:
        temp = "p"
        for i in range(1,len(silaba)):
            temp = temp + silaba[i]
        silaba = silaba + temp
    return silaba

def Converte(palavra:str) -> str:
    """Função que converte uma palavra na lingua dos P"""
    converte = ""
    for i in range(len(palavra)):
        if E_Vogal(palavra[i])==False and i > 0:
            #converter a silaba
            pass
        else:
            converte = converte + palavra[i]