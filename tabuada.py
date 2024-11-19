def Tabuada(n):
    """
    Função que calcula e mostra a tabuda do nº que recebe

    Parametros:
        n: nº inteiro
    Outuput:
        Tabuada de 1 a 10 do n
    """
    for i in range(1,11):
        r = i * n
        print(f"{i} x {n} = {r}")

Tabuada(5)