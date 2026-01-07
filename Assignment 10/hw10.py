#!/usr/bin/env python3

class Wine:
    def __init__(self, vineyard, type, year):
        self.__vineyard = vineyard
        self.__type = type
        self.__year = int(year)
        self.__rating = ""

    def get_vineyard(self):
        return self.__vineyard

    def get_type(self):
        return self.__type

    def get_year(self):
        return self.__year

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def __str__(self):
        return self.__vineyard + " " + self.__type + " " + str(self.__year)

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year



w1 = Wine("Pahkmeyer", "Merlot", 1999)
print("vineyard: ", w1.get_vineyard())
print("type:     ", w1.get_type())
print("year:     ", w1.get_year())
print("rating:   ", w1.get_rating())

w1.set_rating(95)
print(w1)
print("rating:  ", w1.get_rating())

w2 = Wine("Hartwell", "Merlot", 2000)
print(w2)

print("w1 > w2  :", w1 > w2)
print("w1 < w2  :", w1 < w2)
print("w1 == w2 :", w1 == w2)
print("w1 != w2 :", w1 != w2)
