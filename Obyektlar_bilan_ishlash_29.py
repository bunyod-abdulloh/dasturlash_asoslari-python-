

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

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"Ism: {self.ism}, Sharif: {self.sharif}, Tug'ilgan yil: {self.tyil}, Bosqich: {self.bosqich}""'"

    def get_full_name(self):
        return f"{self.ism} {self.sharif}"

    def get_age(self, joriy_yil):
        return joriy_yil - self.tyil

    def tanishtir(self):
        return f"Ismim {self.ism} {self.sharif}, tug'ilgan yilim: {self.tyil}"


talaba1 = Talaba("Olim", "Olimov", 1990)
talaba2 = Talaba("Nariman", "Narimov", 1992)


class Fan():
    pass
