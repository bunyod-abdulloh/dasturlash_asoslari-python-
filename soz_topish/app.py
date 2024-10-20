
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# random_matn = random.sample(alphabet, 5)
random_matn = ['k', 'a', 'l', 'l', 'a']
join_matn = "".join(random_matn).capitalize()
belgi = ''
empty_matn = ''
bad = "l"
for n in random_matn:
    if n == bad:
        belgi += bad
    else:
        belgi += '='

print(random_matn)
print(belgi.upper())

user_letters = ''
user_input = 'Harf kiriting:'
while True:
    user_input = input(f"Harf kiriting: {user_letters}")
    user_letters += user_input.upper()
    print(f'Siz kiritgan harflar: {user_letters}')
    print(user_input)
    print(user_letters)
    if user_input in random_matn:
        print('bor')
