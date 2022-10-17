slownik = {}

wejscie = input("Podaj łańcuch znaków \n")

for i in wejscie:
    if i not in slownik:
        slownik[i]=0
    slownik[i] += 1

print(slownik)