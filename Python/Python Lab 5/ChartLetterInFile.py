def read_file(file_name:str)->str:
    return open(file_name).read()

def count(data:str)->dict:
    output = {}
    for x in data:
        if x.isalpha():
            x = x.lower()
            if x not in output:
                output[x]=0
            output[x]+=1
    return output

def chart(data:dict):
    data = dict(sorted(data.items()))
    for x in range(len(data)):
        m = max(data, key=data.get)
        mValue = data[m]
        key = list(data.keys())[x]
        amount = 50*data[key]/mValue
        print(f"{key} {'*'*int(amount)} {' '*(50-int(amount))} {data[key]}")

p = "C:/Users/szymk/Desktop/ksiazka.txt"
data = read_file(p)
chart(count(data))