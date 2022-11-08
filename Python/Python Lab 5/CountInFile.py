def read(file_name):
    file = open(file_name)
    return file.read()

def licznZnakiSlowa(dane:str):
    ileZnakow = 0
    ileBialych = 0
    for x in dane:
        if x.isspace():
            ileBialych+=1
        ileZnakow+=1
    return [ileZnakow, ileBialych, len(dane.split())]

dane = read("C:/Users/student8.UE/Desktop/tak.txt")
print(licznZnakiSlowa(dane))
