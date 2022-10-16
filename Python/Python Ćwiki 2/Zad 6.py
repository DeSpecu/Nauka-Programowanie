

wejscie = int(input("Podaj n: "))
while(wejscie<0):
    wejscie = int(input("Podaj n: "))

n = wejscie+1

macierz=[[''for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for x in range(1,min(i,j)+1):
            if i%x==0 and j%x==0:
                if x == 1:
                    macierz[i][j]='+'
                else:
                    macierz[i][j]='-'
            
for i in range(n):
    macierz [0][i]=i
    macierz [i][0]=i

for _ in macierz:
    print(f"{_}")
