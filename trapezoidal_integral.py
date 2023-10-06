from math import sin,pi
# --example--
# print(sin(0))
# >>> 0
# -----------

a = 0
b = pi / 2
n = 100
h = (b - a) /n
s = 0

for k in range(n):
    s +=  (h / 2)*(sin(a + k*h) + sin(a + (k+1)*h))
print(s)


