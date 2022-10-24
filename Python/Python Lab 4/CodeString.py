text = input("Podaj ciąg znaków\n")
n = int(input("Podaj n\n"))

while n<1 or n >26:
    print("Podaj n w zakresie 0-26")
    n = int(input("Podaj n\n"))

shift = n%26
i=0

toChange = list(text)

while True:
    value = ord(toChange[i])+shift
    if value>125:
        value-=92
    toChange[i]=chr(value)
    i+=1
    if i>=len(text):
        break
text="".join(toChange)
print(text)

