from math import sqrt
import random as r

# ================ LAMBDA FUNCTIONS ================
# uzunlik = lambda pi, r: 2 * pi * r
# print(uzunlik(math.pi, 10))
#
# kvadrat = lambda x, y: x ** y
# print(kvadrat(3, 2))
#
#
# def daraja(n):
#     return lambda x: x ** n
#
#
# kvadrat_ = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat_(3)} ga, kubi esa, {kub(3)}")


sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)


# def daraja2(x):
#     """Berilgan sonning kvadratini qayratuvchi funksiya"""
#     return x * x
#
#
# print(list(map(daraja2, sonlar)))

# kvadratlar = list(map(lambda x: x*x, sonlar))
# print(kvadratlar)


# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y: x+y, a, b))
# print(a_plus_b)


# ================ FILTER FUNCTION ================
sonlar = r.sample(range(100), 10)
# print(sonlar)
#
#
# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
#     return x % 2 == 0
#
#
# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

# juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar))
# print(juft_sonlar)

mevalar = ['olma', 'anor', 'uzum', 'anjir', 'gilos', 'behi']
harf = 'b'
mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva: meva.startswith('g') and meva.endswith('s'), mevalar))
print(mevalar2)
