from vazifalar.oop_read_txt import get_user_number


class Person:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, birth_year: int, birth_month: int,
                 birth_day: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self._birth_year = birth_year
        self._birth_month = birth_month
        self._birth_day = birth_day

    @property
    def birth_date(self):
        # Tug'ilgan kunni matn formatida qaytaradi
        return f"{self._birth_day:02d}-{self._birth_month:02d}-{self._birth_year}"

    def get_info(self):
        return f"Ism: {self.first_name}\nSharif: {self.last_name}\nYosh: {self.age}\nEmail: {self.email}\nTavallud: {self.birth_date}"

    def get_life_path_number(self):
        birth_date = sum(int(digit) for digit in str(self._birth_day))
        birth_month = sum(int(digit) for digit in str(self._birth_month))
        birth_year = sum(int(digit) for digit in str(self._birth_year))
        first_result = birth_date + birth_month + birth_year
        final_result = sum(int(digit) for digit in str(first_result))
        return final_result


get_first_name = input("Ismingizni kiriting: ")
get_last_name = input("Sharifingizni kiriting: ")
get_age = int(input("Yoshingizni kiriting: "))
get_email = input("Emailingizni kiriting: ")
get_birth_day = int(input("Tug'ilgan kuningizni kiriting (dd): "))
get_birth_month = int(input("Tug'ilgan oyingizni kiriting (mm): "))
get_birth_year = int(input("Tug'ilgan yilingizni kiriting (yyyy): "))

person = Person(get_first_name, get_last_name, get_age, get_email, get_birth_year, get_birth_month, get_birth_day)
info = person.get_info()
life_number = person.get_life_path_number()
tarif = get_user_number(filename="hayot_yuli.txt", number=str(life_number))
print(f"\n\nShaxsiy ma'lumotlaringiz:\n{info}")
print(f"Sizning life_path_numberingiz: {life_number}")
print(f"Numerologiya bo'yicha Sizga beriladigan ta'rif: {tarif}")
