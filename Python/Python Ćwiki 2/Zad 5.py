import random

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
n = int(input("Podaj n: "))

macierz = [[random.randint(a,b) for _ in range(n)] for _ in range(n)]

print(macierz)

sumaPrzekatnej=0
for i in range(n):
    sumaPrzekatnej+=macierz[i][i]

sumaPrzekatnej2=0
for i in range(n):
    sumaPrzekatnej2+=macierz[i][n-1-i]

sumaNaNieparzystych=0
for i in range(n):
    for j in range(n):
        if i%2!=0 and j%2!=0:
            sumaNaNieparzystych+=macierz[i][j]

print("Suma 1 przekątnej: ",sumaPrzekatnej)
print("Suma 2 przekątnej: ",sumaPrzekatnej2)
print("Suma na nieparzystych indeksach: ", sumaNaNieparzystych)


for i in range(n):
    macierz[i] = macierz[i][::-1]
macierz = macierz[::-1]

print(macierz)