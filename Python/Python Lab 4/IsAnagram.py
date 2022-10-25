def czyAnagrqam(t1="",t2=""):
    if len(t1)!=len(t2):
        return False
    t1Copy = t1.upper()
    t2Copy = t2.upper()
    arOfT1 = [x for x in t1Copy if x.isupper()]
    arOfT2 = [y for y in t2Copy if y.isupper()]

    arOfT1.sort()
    arOfT2.sort()
    
    for x in range(len(arOfT1)):
        if(arOfT1[x]!=arOfT2[x]):
            return False
    return True

text1=input("Podaje pierwsze słowo\n")
text2=input("Podaje drugie słowo\n")

print(czyAnagrqam(text1,text2))
