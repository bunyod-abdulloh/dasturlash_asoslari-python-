"""
31.10.2024

Theme: Encapsulation
"""

from uuid import uuid4


class Auto:
    __num_avto = 0

    def __init__(self, make, model, color, year, price, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Auto.__num_avto += 1

    @classmethod
    def get_num_auto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinaning kmga yangi km qo'shish"""

        if km >= 0:
            self.__km += km
        else:
            print("Mashina kmini kamaytirib bo'lmaydi!")


class Bus:
    pass


class Train:
    pass
