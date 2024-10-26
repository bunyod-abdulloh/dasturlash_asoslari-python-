class Talaba():
    def __init__(self, ism, sharif, tyil):
        self.ism = ism
        self.sharif = sharif
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        """Talabaning bosqichini bittaga ko'paytiruvchi metod"""
        self.bosqich += 1

    def get_fullname(self):
        return f"{self.ism} {self.sharif}"

    def get_age(self, joriy_yil):
        return joriy_yil - self.tyil

    def get_info(self):
        return f"{self.ism} {self.sharif}, {self.tyil}, {self.bosqich} - bosqich talabasi"


class Fan:
    """Fan nomli klass"""

    def __init__(self, nomi):
        self.nomi = nomi
        self.count_students = 0
        self.students = []

    def add_students(self, talaba):
        """Fanga talabalarni qo'shish"""
        self.students.append(talaba)
        self.count_students += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [student.get_info() for student in self.students]

    def get_students_count(self):
        """Fanga yozilgan talabalar soni"""
        return self.count_students

    def see_methods(self, klass_nomi):
        return [method for method in dir(klass_nomi) if method.startswith("__") is False]


talaba1 = Talaba("Olim", "Olimov", 1990)
talaba2 = Talaba("Nariman", "Narimov", 1992)
talaba3 = Talaba("Bunyod", "MuhammadAli", 1990)
matematika = Fan("Oliy matematika")
matematika.add_students(talaba1)
matematika.add_students(talaba2)
matematika.add_students(talaba3)
