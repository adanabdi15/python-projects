#!/usr/bin/env python3

class LP:
    def __init__(self, title, label, artist):
        self.title = title
        self.label = label
        self.artist = artist

    def get_title(self):
        return self.title

    def get_label(self):
        return self.label

    def get_artist(self):
        return self.artist

    def print_lp(self):
        print(self.title + ", " + self.label + ", " + self.artist)




lp = LP("The London Concert", "Sony Classical", "Wynton Marsalis")
print(lp.get_title())
print(lp.get_label())
print(lp.get_artist())
lp.print_lp()
