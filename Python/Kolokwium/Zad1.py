def sort(dane):
    return [sorted(dane, key=lambda x: x[i]) for i in range(len(dane))]

lista= [[1,2,9,4],[0,4,1,2],[5,3,0,6],[7,5,2,5]]
r = sort(lista)
print(r)