import utils

# x = utils.ler_numero_inteiro_limites(-10,10,"Introduza um nº inteiro:")
# x = utils.ler_numero_inteiro_limites(0,1000)
# x = utils.ler_numero_inteiro_limites(10)
# x = utils.ler_numero_inteiro_limites(10,None,"Introduza qq coisa:")

# x = utils.ler_numero_decimal("Introduza um preço: ")
# print(x)

x = utils.ler_numero_decimal_limites(-10,10,"Introduza um valor decimal:")
x = utils.ler_numero_decimal_limites(0,10.5)
x = utils.ler_numero_decimal_limites(10.5)
x = utils.ler_numero_decimal_limites(0,None,"Introduza um valor: ")