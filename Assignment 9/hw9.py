#!/usr/bin/env python3

class LP:
    def __init__(self, title, label, artist, released):
        self.__title = title
        self.__label = label
        self.__artist = artist
        self.__released = released

    def get_title(self):
        return self.__title

    def get_label(self):
        return self.__label

    def get_artist(self):
        return self.__artist

    def get_released(self):
        return self.__released

    def __str__(self):
        return (
            self.__title + ", " +
            self.__label + ", " +
            self.__artist + ", " +
            self.__released
        )


lp = LP("The London Concert", "Sony Classical", "Wynton Marsalis", "1994")
print(lp.get_title())
print(lp.get_label())
print(lp.get_artist())
print(lp.get_released())
print(lp)
