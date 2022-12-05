import statistics

dane = [[12,1.34,"Ola",1],["Asia","nic"],[1,1,1,1,1],[5.55,2,3,2],[[],"test"]]
wyjscie = []
domediany = []
for l in dane:
    suma = 0
    for i in l:
        if isinstance(i, int):
            domediany.append(i)
            suma+=i
    if len(domediany)>0:
        wyjscie.append((suma, statistics.median(domediany)))
    else:
        wyjscie.append((suma, 0))
    domediany.clear()

tablicaileintow=[0] * len(dane)

for i in dane:
    for l in range(len(i)):
        if isinstance(i[l], str):
            tablicaileintow[l]+=1
            
print(wyjscie, tablicaileintow)