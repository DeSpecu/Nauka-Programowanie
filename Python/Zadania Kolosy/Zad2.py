def change_phrases(text:str, phrases):
    for i in range(len(phrases)):
        text = text.replace(phrases[i][0],phrases[i][1]).replace(phrases[i][0][0].upper()+phrases[i][0][1:],phrases[i][1][0].upper()+phrases[i][1][1:])
    return text

s =  "Ala ma kota, psa i dom. Kota mam też ja. Psa nie ma nikt, nawet Mama."
f =  [("kota","szczura"),("psa","ogórka"),("ma","xyz")]
print(change_phrases(s, f))