#22-dars *args va **kwargs

def summa(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""

    return x+y+sum(sonlar)


print(summa(10, 15, 1, 3))
