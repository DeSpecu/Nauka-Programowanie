text = input("Podaj ciąg znaków\n")

i=0
sum = 0
while True:
    if text[i].isdigit():
        sum+=int(text[i])
    if i>=len(text)-1:
        break
    i+=1

print(sum)
