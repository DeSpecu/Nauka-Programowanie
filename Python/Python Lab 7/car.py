class Samochod:

    def __init__(self, marka, zuzycie_paliwa) -> None:
        self.marka = marka
        self.zuzycia_plaiwa = zuzycie_paliwa
    
    def koszt(self, km, cena):
        return (km/100)*self.zuzycia_plaiwa*cena

    def wyswietl(self):
        print(f"Marka: {self.marka}, Zużycie paliwa: {self.zuzycia_plaiwa}")
    
class Autobus(Samochod):

    def __init__(self, marka, zuzycie_paliwa, l_miejsc) -> None:
        super().__init__(marka, zuzycie_paliwa)
        self.l_miejsc = l_miejsc
    
    def wyswietl(self):
        print(f"Marka: {self.marka}, Zużycie paliwa: {self.zuzycia_plaiwa} Ilość miejsc: {self.l_miejsc}")

class Ciezarowka(Samochod):

    def __init__(self, marka, zuzycie_paliwa, nosnosc) -> None:
        super().__init__(marka, zuzycie_paliwa)
        self.nosnosc = nosnosc

    def wyswietl(self):
        print(f"Marka: {self.marka}, Zużycie paliwa: {self.zuzycia_plaiwa} Nośność: {self.nosnosc}")
    
s = Samochod("Audi", 6)
a = Autobus("BMW", 8.2, 100)
c = Ciezarowka("Renault", 12.4, 4000)


s.wyswietl()
a.wyswietl()
c.wyswietl()

print(s.koszt(100, 6.5))
print(a.koszt(100, 6.5))
print(c.koszt(100, 6.5))