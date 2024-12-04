"""
O Sr Joaquim precisa de um programa para controlar o nº de clientes e de mesas do seu restaurante.
O programa deve apresentar um menu com as opções:
1. Entrada
2. Saída
3. Estado
4. Terminar
Quando o programa arranca deve ler do utilizador o nº de mesas e o nº de clientes que o restaurante pode receber
De  cada vez que entram clientes devem perguntar quantos clientes estão a entrar e quantas mesas vão ocupar
De cada vez que saíem clientes devem perguntar quantos clientes saíram, quantas mesas libertaram e qual o custo da refeição
A opção estado deve indicar quantas mesas estão livres e ocupadas, quantos clientes estão no restaurante e a percentagem de ocupação (de clientes) e o custo de todas as refeições do clientes que já sairam do restaurante
O programa só deve terminar quando é escolhida a opção 4
O programa não deve permitir entradas de dados que não sejam válidas.
"""
import utils

# def Configurar():
#     """
#     Função para definir a configuração do restaurante (nº mesas e nº de clientes)
#     """
#     pass
def EntradaClientes(max_clientes,n_atual):
    """
    Responsável por registar a entrada dos clientes
    """
    #testar se o restaurante não pode receber mais clientes
    if max_clientes == n_atual:
        print("Restaurante está cheio")
        return 0
    #ler o nº de clientes a entrar
    lugar_livres = max_clientes - n_atual
    entrar = utils.ler_numero_inteiro_limites(1,lugar_livres,"Quantos clientes: ")
    #devolve o nº de clientes que entraram
    return entrar
def EntradaMesas(max_mesas,n_atual):
    """
    Responsável por registar a ocupação das mesas
    """
    #testar se não tem mesas livres
    if max_mesas == n_atual:
        print("Restaurante está cheio")
        return 0
    mesas_livres = max_mesas - n_atual
    entrar = utils.ler_numero_inteiro_limites(1,mesas_livres,"Quantas mesas: ")
    return entrar
def Sair():
    """
    Responsável por registar a saída dos clientes e atualizar o custo total das refeições
    """
    pass
def Estado(max_mesas,max_clientes,mesas,clientes):
    """
    Calcula e mostra os dados estatísticos do estado do restaurante
    """
    print(clientes)
def Menu():
    #nº máximo de mesas e clientes que o restaurante pode utilizar
    n_max_mesas    = utils.ler_numero_inteiro("Quantas mesas tem o restaurante: ")
    n_max_clientes = utils.ler_numero_inteiro("Quantos clientes podem estar no restaurante: ")
    op = 1
    #nº de mesas e clientes atualmente no restaurante
    n_atual_mesas    = 0
    n_atual_clientes = 0
    while op != 4:
        op = utils.ler_numero_inteiro_limites(1,4,"1.Entrada\n2.Saída\n3.Estado\n4.Terminar")
        if op == 1:
            #Entrada dos clientes
            n_clientes_entraram = EntradaClientes(n_max_clientes,n_atual_clientes)
            n_mesas_ocupadas    = EntradaMesas(n_max_mesas,n_atual_mesas)
            n_atual_clientes    = n_atual_clientes + n_clientes_entraram
            n_atual_mesas       = n_atual_mesas +  n_mesas_ocupadas
        if op == 3:
            Estado(n_max_mesas,n_max_clientes,n_atual_mesas,n_atual_clientes)

def Main():
    Menu()
if __name__=='__main__':
    Main()