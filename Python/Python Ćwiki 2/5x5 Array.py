import random
n=5
macierz = [[random.randint(-5,5) for _ in range(n)] for _ in range(n)]

print("Macierz: ",macierz)

y = None
indeks = 0
najwieksze = []
najmniejsze = []
for x in range(n):
    for i in macierz:
        if y is None or i[indeks]>y:
            y=i[indeks]
    najwieksze.append(y)
    y=None
    indeks+=1

indeks=0
for x in range(n):
    for i in macierz:
        if y is None or i[indeks]<y:
            y=i[indeks]
    najmniejsze.append(y)
    y=None
    indeks+=1

print("Maksimum dla każdej kolumny: ",najwieksze)
print("Minimum dla każdej kolumny: ",najmniejsze)