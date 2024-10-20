#22-dars *args va **kwargs
#
# def summa(x, y, *sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#
#     return x + y + sum(sonlar)
#
#
# print(summa(10, 15, 1, 3))


def avto_info(kompaniya, model, **malumotlar):
    """Avtomobil malumotlarini lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar


avto1 = avto_info(kompaniya='GM', model='Malibu', rang='qora', yil=2024)
avto2 = avto_info(kompaniya='GM', model='Malibu', rang='yashil', yil=2024, korobka='avtomat')
print(avto1)
print(avto2)
