
def Somar(x,y):
    print(x+y)
    x = 0
    y = 0

def main():
    Somar('joaquim','maria')
    Somar(10,5)
    Somar(10.3,-3.2)
    n = 10
    z = 15
    Somar(n,z)
    print(n,z)

if __name__ == '__main__':
    main()