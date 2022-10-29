import random

#Zadanie 4
def blad(a,b) -> float:
    bledy = 0
    for x in range(len(a)):
        if a[x]!=b[x]:
            bledy+=1
    return bledy/len(a)

dataDic = {}
doYouWant = "t"

while doYouWant=="t":
    word = input("Podaj słowo\n")
    if word in dataDic:
        print("Jest już w słowniku")
        continue
    definition = input("Podaj definicje\n")
    if word not in dataDic:
        dataDic[word] = definition
    doYouWant = input("Czy chcesz dalej dodawać t/n\n")

right = 0
wrong = 0

for i in range(len(dataDic)):
    randomKey = list(dataDic.keys())[random.randint(0, len(dataDic)-1)]
    print("Podaj definicję: ", randomKey)
    guess = input()

    if guess == dataDic[randomKey]:
        right += 1
    else:
        wrong += 1
        print(f"Twój błąd wynosi: {blad(dataDic[randomKey],guess)}")


print("Punkty: ",right, "Błędne: ", wrong)

