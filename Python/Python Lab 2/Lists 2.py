from random import randint


l=[randint(1,10) for _ in range(20)]
print("wylosowane liczby: ",l)
print("wystapienia:")

for e in range(1,11):
     print(e,"-",l.count(e))