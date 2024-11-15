"""
10/02/2021

Dasturlash asoslari

#33-DARS. FILES

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
with open("salommatn.txt") as file:
    pi = file.read()

print(pi)

pi = pi.rstrip()
pi = pi.replace("\n", "")

print(pi)

filename = "salommatn.txt"
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)
