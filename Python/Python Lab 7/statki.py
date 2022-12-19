class Statek:
    def __init__(self, wspolrzedne1, wspolrzedne2) -> None:
        self.wspolrzedne1 = wspolrzedne1
        self.wspolrzedne2 = wspolrzedne2
        self.maszt = True
    
    def strzal(self, wsp1, wsp2):
        if wsp1 == self.wspolrzedne1 and wsp2 == self.wspolrzedne2:
            self.maszt = False
        
        if not self.maszt:
            return 2
        else:
            return 0
        
    def wyswietl(self):
        print(f"Maszt 1: {self.wspolrzedne1}, {self.wspolrzedne2}")
    

class Statek2(Statek):
    def __init__(self, wspolrzedne1, wspolrzedne2) -> None:
        super().__init__(wspolrzedne1, wspolrzedne2)
        self.maszt = True
        self.maszt2 = True

    def strzal(self, wsp1, wsp2):
        trafienie = False
        if wsp1 == self.wspolrzedne1 and wsp2 == self.wspolrzedne2:
            self.maszt = False
            trafienie = True
        elif wsp1 == self.wspolrzedne1 and wsp2 == self.wspolrzedne2+1:
            self.maszt2 = False
            trafienie = True
        if not self.maszt and not self.maszt2:
            return 2
        if trafienie:
            return 1        
        else:
            return 0
        
    def wyswietl(self):
        print(f"Maszt 1: {self.wspolrzedne1}, {self.wspolrzedne2}  Maszt 2: {self.wspolrzedne1}, {self.wspolrzedne2+1}")

class Statek3(Statek):
    def __init__(self, wspolrzedne1, wspolrzedne2) -> None:
        super().__init__(wspolrzedne1, wspolrzedne2)
        self.maszt = True
        self.maszt2 = True
        self.maszt3 = True

    def strzal(self, wsp1, wsp2):
        trafienie = False
        if wsp1 == self.wspolrzedne1 and wsp2 == self.wspolrzedne2:
            self.maszt = False
            trafienie = True
        elif wsp1 == self.wspolrzedne1 and wsp2 == self.wspolrzedne2+1:
            self.maszt2 = False
            trafienie = True
        elif wsp1 == self.wspolrzedne1 and wsp2 == self.wspolrzedne2+2:
            self.maszt3 = False
            trafienie = True
        
        if not self.maszt and not self.maszt2 and not self.maszt3:
            return 2
        if trafienie:
            return 1
        
        return 0

    def wyswietl(self):
        print(f"Maszt 1: {self.wspolrzedne1}, {self.wspolrzedne2}  Maszt 2: {self.wspolrzedne1}, {self.wspolrzedne2+1}  Maszt 3: {self.wspolrzedne1}, {self.wspolrzedne2+2}")

s1 = Statek(1,1)
s2 = Statek2(2,1)        
s3 = Statek3(3,1)

print(s1.strzal(1,1))
print(s2.strzal(2,2))
print(s3.strzal(3,1))
print(s3.strzal(3,0))
print(s3.strzal(3,2))
print(s3.strzal(3,3))

s1.wyswietl()
s2.wyswietl()
s3.wyswietl()