#variável global
g_resultado = 0

def Soma(x,y):
    global g_resultado
    g_resultado = x + y #está a utilizar a variável global

Soma(10,5)
print(g_resultado)