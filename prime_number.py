import math

a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
#61と10が素数でないことを確認するコード

def isprime(n):
    if n<=1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def printprime(n):
    if isprime(n):
        print("Prime number")
    else:
        print("Not prime number")

printprime(a)
printprime(b)
