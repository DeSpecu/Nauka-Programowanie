def read_all_lines_file(file_name):
    lines = open(file_name).readlines()
    return lines

def save(file_name, dane):
    file = open(file_name, 'w+')
    file.write(str(dane))

def szukaj(nazwaPlikWe:str , nazwaPlikWy:str, slowo):
    i = 1
    wyjscie=""
    for x in nazwaPlikWe:
        slowa = x.split()
        for y in slowa:
            if y.find(slowo)>=0:
                wyjscie = wyjscie+str(i)+": "+x
        i+=1

    save(nazwaPlikWy, wyjscie)



dane = read_all_lines_file("C:/Users/student8.UE/Desktop/tak.txt")
wyjscie = ("C:/Users/student8.UE/Desktop/tak2.txt")
szukane = input("Podaj slowo\n")
szukaj(dane, wyjscie, szukane)
