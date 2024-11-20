def MaiorDeDois(n1,n2):
    if n1 == n2:
        return None
    elif n1 > n2:
        return n1
    elif n2 > n1:
        return n2

assert MaiorDeDois(10,5) == 10,"A função devia devolver 10"
assert MaiorDeDois(5,10) == 10,"A função devia devolver 10"
assert MaiorDeDois(10,10) == None, "A função devia devolver None porque o nº são iguais"
print("A função passou todos os testes")