import math
class wektor:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def dlugosc(self):
        return math.sqrt(self.x**2+self.y**2)
    def normalizuj(self):
        return wektor(self.x/self.dlugosc(), self.y/self.dlugosc())
    def wyswietl(self):
        print(f"Wektor[{self.x},{self.y}] o długości {self.dlugosc()}")
