def read_all_lines_file(file_name):
    lines = open(file_name).readlines()
    return lines
def save(file_name, dane):
    file = open(file_name, 'a+')
    file.write(str(dane))
    file.write("\n")

def sumujIZapisz(nazwaPliku:str):
    wyjscie=0
    for x in nazwaPliku:
        wyjscie+=int(x)

    return wyjscie+1



dane = read_all_lines_file("C:/Users/student8.UE/Desktop/tak.txt")
wyjscie = ("C:/Users/student8.UE/Desktop/tak2.txt")
save(wyjscie, sumujIZapisz(dane))
