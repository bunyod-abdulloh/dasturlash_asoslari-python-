import random


# Username generatsiya qiluvchi funksiya
def user_name():
    """ Username generatsiya qiluvchi funksiya """

    text = input("Ismingizni kiriting: ")
    reversed_text = text[::-1].lower()
    get_number = random.randint(0, 9)
    return f"{reversed_text}{get_number}"


sonlar_ = ['5', '5', '5']


def convert_add(sonlar: list):
    """ Foydalanuvchidan matn shaklidagi raqamlarni qabul qilib yig'indisini chiqarib beruvchi funksiya """
    summary = int()
    for son in sonlar:
        summary += int(son)

    return summary


converted_numbers = convert_add(sonlar_)
print(converted_numbers)
