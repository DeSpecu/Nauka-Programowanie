def HTMLColor2RGB(color:str) -> list:
    if len(color)!=7:
        return "Bledne dane"
    i=1
    output = []
    while i < len(color):
        h=color[i]+color[i+1]
        d = int(h, base=16)
        output.append(d)
        i+=2
    return output

wejscie = input("Podaj kolor\n")

print(HTMLColor2RGB(wejscie))
