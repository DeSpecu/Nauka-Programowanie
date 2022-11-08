def read_file(file_name):
    lines = open(file_name).read()
    return lines
def save(file_name, dane):
    file = open(file_name, 'a+')
    file.write(str(dane))
    file.write("\n")

def szyfruj(text:str, n:int)->str:
    shift = n % 26
    i = 0
    toChange = list(text)

    while True:
        value = ord(toChange[i]) + shift
        if value > 125:
            value -= 92
        toChange[i] = chr(value)
        i += 1
        if i >= len(text):
            break
    text = "".join(toChange)
    return text
p = "C:/Users/student8.UE/Desktop/tak.txt"
p=p.split('/')
p="/".join(p[:-1]+["_"+p[-1]])
dane = read_file("C:/Users/student8.UE/Desktop/tak.txt")
n = input("Przesuniecie\n")
save(p, szyfruj(dane, int(n)))
