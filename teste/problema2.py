
def CalcularPreco(preco,divisa) -> float:
    """
    Calcula o preço do produto no pais
    """
    taxa = 0
    taxa_alfandega = 0
    if divisa.lower()=='r':
        taxa = 4.05
        taxa_alfandega = 0.1
    elif divisa.lower()=='d':
        taxa = 1.23
        taxa_alfandega = 0.1
    elif divisa.lower()=='l':
        taxa = 0.89
    else:
        taxa = 4.67 
    preco_convertido = preco * taxa
    preco_convertido = preco_convertido + (preco_convertido * taxa_alfandega)
    return round(preco_convertido,2)

def NomeDivisa(divisa) -> str:
    """
    Devolve o nome da divisa por extenso
    """
    texto = ""
    if divisa.lower()=="r":
        texto = "Reais [Brasil]"
    elif divisa.lower()=="d":
        texto = "Dólares [EUA]"
    elif divisa.lower()=="l":
        texto = "Libras Esterlinas [UK]"
    else:
        texto = "Liras Turcas [Turquia]"
    return texto

def MostraTaxas():
    """
    Mostra as taxas de conversão
    """
    print("Taxas:\nR->4,05\nD->1,23\nL->0,89\nT->4,67")

def Main():
    op = input("Consultar taxas? (s/n)")
    preco = float(input("Preço do produto (Euros):"))
    if preco<=0:
        print("O preço tem de ser um valor positivo")
        return
    divisa = input("Divisa (R/D/L/T):")
    if divisa.lower() not in "rdlt":
        print("A divisa tem de ser uma de R D L T")
        return
    if op.lower() == "s":
        MostraTaxas()
    preco_convertido = CalcularPreco(preco,divisa)
    print(f"Preço do produto: {preco_convertido} {NomeDivisa(divisa)}")

if __name__=='__main__':
    Main()