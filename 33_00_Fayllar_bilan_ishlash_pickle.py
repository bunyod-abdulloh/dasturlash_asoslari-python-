

with open('salommatn.txt') as file:
    """ Fayllar bu ko'rinishda ochilganda doim str shaklda o'qiladi """
    text = file.read()

text = text.rstrip()
text = text.replace('\n', ' ').capitalize()

print(text)
