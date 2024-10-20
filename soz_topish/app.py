
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

random_matn = random.sample(alphabet, 5)
join_matn = "".join(random_matn).capitalize()
belgi = ''
empty_matn = ''

for n in range(len(join_matn)):
    belgi += '='
print(join_matn)
print(belgi)
