def stringToInt(text=""):

    arrayForDigit = []

    for c in text:
        if c.isdigit() or c in ['+','-','e']:
            arrayForDigit.append(c)
        else:
            break
    for ch in arrayForDigit:
        

