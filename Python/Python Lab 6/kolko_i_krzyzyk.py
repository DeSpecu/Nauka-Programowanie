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
 
    def sprawdz_kolumne(self):
        for x in range(self.wielkosc):
            for y in range(self.wielkosc):
                if self.__plansza[x][0] == self.__plansza[x+1][0]:
                    return False
                if self.__plansza[x][y] != self.__plansza[x][y+1]:
                    return False      
        return True

    def sprawdz_wiersz(self):
        for x in range(self.wielkosc):
            for y in range(self.wielkosc-1):
                if self.__plansza[x][y] != self.__plansza[x][y+1]:
                    return False    
        return True
 
    def zagraj(self):
        while True:
            self.wyswietl()
            print(f"Tura {self.symbol()}")
            wiersz = input("Podaj wiersz\n")
            while int(wiersz) > self.wielkosc:
                wiersz = input(f"Podaj wiersz mniejszy od {self.wielkosc}\n")
            kolumna = input("Podaj kolumnę\n")
            while int(kolumna) > self.wielkosc:
                kolumna = input(f"Podaj kolumnę mniejszą od {self.wielkosc}\n")
            self.__plansza[int(wiersz)-1][int(kolumna)-1] = self.symbol()
            self.wyswietl()
            self.__symbol = not self.__symbol
            if self.sprawdz_kolumne():
                self.__symbol = not self.__symbol
                print(f"Wygrał {self.symbol()}")
                break

rozmiar = input("Podaj wielkość planszy\n")
p = Plansza(int(rozmiar))
p.zagraj()