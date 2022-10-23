
liczba = input("Podaj liczbę\n")

def num_to_write(liczba):
    dziesiatki ={20:"dwadzieścia",30:"trzydzieści",40:"czterdzieści",50:"pięćdzisiąt",60:"sześćdziesiąt",70:"siedemdziesiąt",80:"osiemdziesiąt",90:"dziewięćdziesiąt"}
    setki = {100:"sto", 200:"dwieście",300:"trzysta",400:"czterysta",500:"pięćset",600:"sześćset",700:"siedemset",800:"osiemset",900:"dziewięćset"}
    liczbyDo20={1:"jeden",2:"dwa",3:"trzy",4:"cztery",5:"pięć",6:"sześć",7:"siedem",8:"osiem",9:"dziewięć", 10:"Dziesięć",
    11:"jedenaście",12:"dwanaście",13:"trzynaście",14:"czternaście",15:"piętnaście",16:"szesnaście", 17:"siedemnaście",18:"osiemnaście",19:"dziewiętnaście"}


    tysiac = 1000
    milion = tysiac*1000

    if liczba<20:
        return liczbyDo20[liczba]
    
    if liczba<100:
        if liczba % 10 == 0:
            return dziesiatki[liczba]
        else:
            return dziesiatki[liczba//10*10] + " "+ liczbyDo20[liczba%10]

    if liczba<tysiac:
        if liczba%100==0:
            return setki[liczba]
        return setki[liczba//100*100] + " " + num_to_write(liczba%100)

    if liczba<milion:
        if liczba%tysiac==0:
            return num_to_write(liczba//tysiac) + " tysięcy"
        else:
            return num_to_write(liczba//tysiac) + " tysięcy " + num_to_write(liczba%tysiac)

    if liczba==milion:
        return "Milion"

    if liczba>milion:
        return "Obsługiwane liczby to 1 - 1.000.000"


print(num_to_write(int(liczba)))

