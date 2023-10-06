a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

# gcd: Greatest Common Diviser

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b) #再帰定義

def gcd2(a, b): #a,bが互いに素であるかを判定する関数
    if gcd(a,b)==1:
        return True 
    else:
        return False
print(gcd(a, b))
print(gcd2(a, b))

#bが0になるまで再帰的に自分自身を呼び出し、bが0になればaが最大公約数である   