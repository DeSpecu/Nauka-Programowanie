import os

def count_words(path):
    subdirs = [x[0] for x in os.walk(path)]
    subdirs.remove(path)
    
    endof = []
    for x in subdirs:
        output = {}
        for filename in os.listdir(x):
            fileB = open(os.path.join(x, filename), "r", encoding="utf-8")
            text = fileB.read().replace(",", "").replace(".","").replace("\n","").casefold().split()
            for word in text:
                if len(word)>2:
                    if word not in output:
                        output[word]=0
                    output[word] +=1
        endof.append(output)
        fileB.close()
    return endof

print(count_words("C:/Users/mario/Downloads/ksiazki"))