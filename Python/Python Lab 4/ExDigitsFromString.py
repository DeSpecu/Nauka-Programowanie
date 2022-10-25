
def stringToInt(text=""):

    dataForDigit = ""

    for c in text:
        if c.isdigit() or c in ['+','-','e']:
            dataForDigit += c
        else:
            break
    return dataForDigit

text = input("Podaj tekst\n")
data = stringToInt(text)

output = ""
power=""

if len(data)>0:
    if data[0]=="-":
        output+="-"
    else:
        output+=data[0]
    for x in range(1,len(data)):
        if data[x]=="-":
            break
        if data[x].isdigit():
            output += data[x]
        if data[x] == "e" and x<len(data)-1:
            power = data[x + 1:]
            if power.count("-")==0:
                output = int(output) * (10 ** int(power))
            break

elif len(data)==0:
    output="0";


print(output)
