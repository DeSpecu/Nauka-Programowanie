import random

listn = []

for i in range(10):
    listn.append(random.randrange(-10,10))
print(listn)

#Min/Max
minimalny = min(listn)
maksymalny = max(listn)
print("Min= ",minimalny)
print("Max= ",maksymalny)

y = None
for i in listn:
    if y is None or i>y:
        y=i
print(y)

x = None
for i in listn:
    if x is None or i<x:
        x=i
print(x)

#AVG
wynik = 0
for i in listn:
    wynik += i

srednia = wynik/len(listn)
print("Średnia:",srednia)

mniejszych=0
wiekszych=0
for i in listn:
    if i>srednia:
        wiekszych+=1
    elif i<srednia:
        mniejszych+=1
print("Większych niż średnia:",wiekszych)
print("Mniejszych niż średnia:",mniejszych)
print(listn[::-1])




