import re

class Plansza:
    def __init__(self, wielkosc):
        self.wielkosc = wielkosc
        self.__plansza = [["-" for x in range(wielkosc)] for x in range(wielkosc)]
        self.__symbol = False # True - X, False - O
 
    def wyswietl(self):
        print("="*(self.wielkosc*2-1))
        for wiersz in self.__plansza:
            for krotka in wiersz:
                print(krotka, end=" ")
            print()
        print("="*(self.wielkosc*2-1))
 
    def symbol(self):
        if self.__symbol:
            return "X"
        return "O"
 
    def sprawdz(self):

        row, column, diagonal, diagonal2 = "", "", "", ""
        change = 0
        for x in range(self.wielkosc):
            rowchecked = x
            for y in range(self.wielkosc):

                if y+change < self.wielkosc and rowchecked < self.wielkosc:
                    diagonal += self.__plansza[rowchecked][y+change]
                    diagonal2 += self.__plansza[rowchecked][self.wielkosc-(y+change)-1]
                rowchecked += 1
                
                row += self.__plansza[x][y]
                column += self.__plansza[y][x]

            match =  re.search(f"{self.symbol()}"*5,row)
            if match is not None:
                return True
            match =  re.search(f"{self.symbol()}"*5,column)
            if match is not None:
                return True
            match =  re.search(f"{self.symbol()}"*5,diagonal)        
            if match is not None:
                return True
            match =  re.search(f"{self.symbol()}"*5,diagonal2)
            if match is not None:
                return True

            row = ""
            column = ""
            diagonal = ""
            diagonal2 = ""

        return False
    
    def czypuste(self,x, y):
        if self.__plansza[int(x)-1][int(y)-1] != "-":
            return False
        return True
 
    def zagraj(self):
        tury = 0
        while True:
            tury+=1
            if tury>self.wielkosc**2:
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
            if self.sprawdz():
                self.wyswietl()
                print(f"Wygrał {self.symbol()}")
                break
            self.__symbol = not self.__symbol

rozmiar = input("Podaj wielkość planszy\n")
p = Plansza(int(rozmiar))
p.zagraj()
