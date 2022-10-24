text = input("Podaj ciąg znaków\n")


howMany = 0
for c in text:
    if c==text[len(text)-1]:
        howMany+=1

print(howMany)
