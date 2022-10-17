import math


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

nieparzyste = []
for i in range(a,b):
    if i%2!=0:
        nieparzyste.append(i)

for i in range(len(nieparzyste)):
    nieparzyste[i] = (nieparzyste[i],2**nieparzyste[i],math.sqrt(nieparzyste[i]))

print(nieparzyste)