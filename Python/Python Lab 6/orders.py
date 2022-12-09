class element_zamowienia:

    def __init__(self, nazwa = "Chleb", cena = 4.00, sztuki = 6):
        self.nazwa = nazwa
        self.cena = cena
        self.sztuki = sztuki

    def __str__(self):
        return f"{self.nazwa} {self.cena}zł, {self.sztuki} szt., łącznie: {self.oblicz_rabat()*self.sztuki}zł"

    def oblicz_koszt(self):
        return self.sztuki*self.oblicz_rabat()

    def oblicz_rabat(self):
        return self.cena*0.9 if self.sztuki > 4 else self.cena

class zamowienia:
    __elementy = []
    __rozmiar = 0
    __maks_rozmiar = 0
    def __init__(self, maks_rozmiar):
        self.__maks_rozmiar = maks_rozmiar
    
    def dodaj(self, elZam):
        if self.__maks_rozmiar <= self.__rozmiar:
            return False
        else:
            self.__elementy.append(elZam)
            self.__rozmiar += 1
            return True
    
    def oblicz_koszt(self):
        suma  = 0
        for x in self.__elementy:
            suma += x.oblicz_koszt()
        return suma

    def pisz(self):
        rabat = 0
        for x in self.__elementy:
            print(x)
            rabat += x.cena*x.sztuki-x.oblicz_koszt()
        print(f"Łączny koszt: {self.oblicz_koszt()}zł")
        print(f"Naliczony rabat: {rabat}")

z = zamowienia(10)
z.dodaj(element_zamowienia("Chleb", 4.0, 2))
z.dodaj(element_zamowienia("Mleko", 2.5, 1))
z.dodaj(element_zamowienia("Cukier", 4.0, 5))
z.dodaj(element_zamowienia("Puszka", 9.0, 1))
z.pisz()
