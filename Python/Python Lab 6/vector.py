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
    def __add__(self, other):
        return wektor(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return wektor(self.x - other.x, self.y - other.y)
    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self
    def __isub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self
    def __str__(self):
        return f"Wektor[{self.x},{self.y}] o długości {self.dlugosc()}"
    def __mul__(self, a):
        return wektor(self.x * a, self.y * a)
    def __rmul__(self, a):
        self.x = self.x * a
        self.y = self.y * a
        return self

w = wektor(2,4)
w2 = wektor(1.5)
print(w)
print(w2)
print("W1+W2", w+w2)
print("W1-W2", w-w2)
print("W1*W2", w*2)
print("-3*W2", w2*-3)
print("W1*2-W2", w*2-w2)
print("W1 po normalizacji", w.normalizuj())
print("W2 po normalizacji", w2.normalizuj())
w.wyswietl()
w2.wyswietl()
