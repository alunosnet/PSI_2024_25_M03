def MDC(n1,n2):
    """
    Calcula o máximo divisor comum entre dois nº
    Recebe:
        dois nº inteiros positivos
    Devolve:
        None: se não existir nenhum
        Nº: que é o MDC
    """
    #encontrar o menor nº
    menor = n1
    if n2 < menor:
        menor = n2
    maior_divisor = None
    for i in range(2,menor):
        if n1 % i == 0 and n2 % i == 0:
            maior_divisor = i
    return maior_divisor

assert MDC(5, 10) == None, "Não existe MDC entre 5 e 10"
assert MDC(6,12) == 3, "O MDC de 6 e 12 é 3"
assert MDC(12,6) == 3, "O MDC de 6 e 12 é 3"
assert MDC(12,18) == 6, "O MDC de 12 e 18 é 6"
assert MDC(10,20) == 5, "O MDC de 10 e 20 é 5"
print("A função passou todos os testes")