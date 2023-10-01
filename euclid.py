a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

# gcd: Greatest Common Diviser

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b) #再帰定義
print(gcd(a, b))

#bが0になるまで再帰的に自分自身を呼び出し、bが0になればaが最大公約数である   