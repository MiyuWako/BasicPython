from math import exp, sin,pi
# --example--
# print(sin(0))
# >>> 0
# -----------

#a = 0
#b = pi / 2
#n = 100

def integral(f, a=0, b=1, n=100):
    s = 0
    h = (b - a) /n
    for k in range(n):
        s +=  (h / 2)*(f(a + k*h) + f(a + (k+1)*h))
    return s

def f1(x):
    return sin(x)
def f2(x):
    return 4/(1+x**2)
def f3(x):
    return (pi**(1/2))*exp(-x*x)
print("(1)の積分値は")
print(integral(f1, 0, pi/2, 50))

print("(2)の積分値は")
print(integral(f2, 0, 1, 100))

print("(3)の積分値は")
print(integral(f3, -100, 100, 1000))
