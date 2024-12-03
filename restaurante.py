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
def Entrada():
    """
    Responsável por ler o nº de clientes e de mesas e registar a entrada dos clientes
    """
    pass
def Sair():
    """
    Responsável por registar a saída dos clientes e atualizar o custo total das refeições
    """
    pass
def Estado():
    """
    Calcula e mostra os dados estatísticos do estado do restaurante
    """
    pass
def Menu():
    n_mesas    = utils.ler_numero_inteiro("Quantas mesas tem o restaurante: ")
    n_clientes = utils.ler_numero_inteiro("Quantas clientes podem estar no restaurante: ")
    op = 1
    while op != 4:
        op = utils.ler_numero_inteiro_limites(1,4,"1.Entrada\n2.Saída\n3.Estado\n4.Terminar")
        

def Main():
    Menu()
if __name__=='__main__':
    Main()