text = input("Podaj ciąg znaków\n")

i=0
while True:
    if i>=len(text):
        i=0
        break
    elif text[i]!=text[len(text)-1-i]:
        break
    i+=1

if i==0:
    print("Palindrom")
else:
    print("Nie")
