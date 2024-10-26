

class Talaba():
    def __init__(self, ism, sharif, tyil):
        self.ism = ism
        self.sharif = sharif
        self.tyil = tyil

    def get_full_name(self):
        return f"{self.ism} {self.sharif}"

    def get_age(self, joriy_yil):
        return joriy_yil - self.tyil

    def tanishtir(self):
        return f"Ismim {self.ism} {self.sharif}, tug'ilgan yilim: {self.tyil}"


talaba1 = Talaba("Olim", "Olimov", 1990)
talaba2 = Talaba("Nariman", "Narimov", 1992)
