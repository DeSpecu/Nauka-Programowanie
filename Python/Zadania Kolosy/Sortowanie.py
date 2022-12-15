def sortuj(s:str):
    nowys = ""
    for i in range(len(s)):
        if s[i] not in [',', '.']:
            nowys+=s[i]
    dlugosc=0
    dopetli = nowys.split()
    for c in dopetli:
        dlugosc+=len(c)
    
    dopetli = sorted(dopetli, key=str.casefold)

    wyjscie=""
    for i in dopetli:
        wyjscie+=i
        wyjscie+=" "
    return wyjscie + str(dlugosc/len(dopetli))


print(sortuj("Aleksandra, Joanna, Agnieszka."))

print(sortuj("Ala ma kota i dwie agrafki."))