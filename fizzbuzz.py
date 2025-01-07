#Exercício fizzBuzz

def fizzBuzz(upTo):
    for n in range(1,upTo+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz",end=" ")
        elif n % 3 == 0:
            print("Fizz",end=" ")
        elif n% 5 == 0:
            print("Buzz",end=" ")
        else:
            print(n, end=" ")

def fizzBuzz_v2(upTo):
    for n in range(1,upTo+1):
        if n % 15 == 0:
            print("FizzBuzz",end=" ")
        elif n % 3 == 0:
            print("Fizz",end=" ")
        elif n% 5 == 0:
            print("Buzz",end=" ")
        else:
            print(n, end=" ")

def fizzBuzz_v3(upTo):
    for n in range(1,upTo+1):
        print("FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n),end=" ")

fizzBuzz(35)
print("-------------------------------")
fizzBuzz_v2(35)
print("------------------------------")
fizzBuzz_v3(35)