def read_all_lines_file(file_name):
    lines = open(file_name).readlines()
    return lines

def save(file_name, dane):
    file = open(file_name, 'a+')
    file.write(str(dane))
    file.write("\n")

def male(names:list):
    output = []
    for x in names:
        data = x.split(" ")
        if data[2] == "M":
            output.append(f"{data[1]} {data[0]} {65-int(data[3])}")
    return output

def female(names:list):
    output = []
    for x in names:
        data = x.split(" ")
        if data[2] == "K":
            output.append(f"{data[1]} {data[0]} {60-int(data[3])}")
    return output


p = "C:/Users/szymk/Desktop/test.txt"
data = read_all_lines_file(p)
males = male(data)
females = female(data)
p=p.split('/')
p="/".join(p[:-1]+["m"+p[-1]])
save(p, males)
p=p.split('/')
p="/".join(p[:-1]+["f"+p[-1]])
save(p, females)