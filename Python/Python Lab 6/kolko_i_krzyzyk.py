class Plansza:
    def __init__(self, wielkosc=3):
        self.wielkosc = wielkosc
        self.__plansza = [["-" for x in range(wielkosc)] for x in range(wielkosc)]
        self.__symbol = False # True - X, False - O
 
    def wyswietl(self):
        print("="*(self.wielkosc+3))
        for wiersz in self.__plansza:
            for krotka in wiersz:
                print(krotka, end=" ")
            print()
        print("="*(self.wielkosc+3))
 
    def symbol(self):
        if self.__symbol:
            return "X"
        return "O"
 
    def sprawdz(self):
        
        for x in range(self.wielkosc):
            if "-" != self.__plansza[x][0] == self.__plansza[x][1] == self.__plansza[x][2] or "-" != self.__plansza[0][x] == self.__plansza[1][x] == self.__plansza[2][x]:
                return True
        if "-" != self.__plansza[0][0] == self.__plansza[1][1] == self.__plansza[2][2] or "-" != self.__plansza[0][2] == self.__plansza[1][1] == self.__plansza[2][0]:
            return True
        
        return False
    
    def czypuste(self,x, y):
        if self.__plansza[int(x)-1][int(y)-1] != "-":
            return False
        return True
 
    def zagraj(self):
        tury = 0
        while True:
            tury+=1
            if tury>9:
                print("Remis")
                break
            self.wyswietl()
            print(f"Tura {self.symbol()}")
            wiersz = input("Podaj wiersz\n")
            while int(wiersz) > self.wielkosc:
                wiersz = input(f"Podaj wiersz mniejszy od {self.wielkosc}\n")
            kolumna = input("Podaj kolumnę\n")
            while int(kolumna) > self.wielkosc:
                kolumna = input(f"Podaj kolumnę mniejszą od {self.wielkosc}\n")
            if self.czypuste(wiersz,kolumna):
                self.__plansza[int(wiersz)-1][int(kolumna)-1] = self.symbol()
            else:
                print("Miejsce zajęte")
                break
            self.wyswietl()
            self.__symbol = not self.__symbol
            if self.sprawdz():
                self.__symbol = not self.__symbol
                print(f"Wygrał {self.symbol()}")
                break
#Do kolejnego zadania
#rozmiar = input("Podaj wielkość planszy\n")
p = Plansza(3)
p.zagraj()
