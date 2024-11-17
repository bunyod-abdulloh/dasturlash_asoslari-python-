from unicodedata import digit


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
        return f"Ism: {self.first_name}\nSharifi: {self.last_name}\nYosh: {self.age}\nEmail: {self.email}\nTavallud: {self.birth_date}"

    def get_life_path_number(self):
        birth_date = sum(int(digit) for digit in str(self._birth_day))
        birth_month = sum(int(digit) for digit in str(self._birth_month))
        birth_year = sum(int(digit) for digit in str(self._birth_year))
        first_result = birth_date + birth_month + birth_year
        final_result = sum(int(digit) for digit in str(first_result))
        return f"{self.first_name}ni life_path_numberi bu {final_result}"


person = Person("Hasan", "ibn Husan", 25, "hasanhusan@example.com", 2000, 6, 15)
# print(person.first_name)
# print(person.last_name)
# print(person.age)
# print(person.email)
# print(person.birth_day)

# print(person.get_info())
print(person.get_life_path_number())
