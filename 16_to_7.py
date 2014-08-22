def hextodec(x):
    if x == 0:
        decNum = 0
    while True:
        if not str(x).isdigit():
            sign = " "
            x = list(x)
            if any(sign !="A" and sign !="B" and sign !="C" and sign !="D" and sign !="E" and sign !="F" and sign != "1" and sign !="2" and sign !="3" and sign !="4" and sign !="5" and sign !="6"
            and sign !="7" and sign !="8" and sign !="9" and sign != "0" for sign in x): # Не придумал пока ничего лучшего...
                print("Недопустимое значение!")
                x = input("... ")
                continue
            else:
                break
        else:
            break
    maxExp = len(x) - 1
    i = 0
    a = 0
    inter = 0
    decNum = False
    while i <= maxExp:
        a = x[i]
        if not a.isdigit():
            a = ord(a) # И здесь тоже.
            if a == 65:
                a = 10
            elif a == 66:
                a = 11
            elif a == 67:
                a = 12
            elif a == 68:
                a = 13
            elif a == 69:
                a = 14
            elif a == 70:
                a = 15
        else:
            a = x[i]
        inter = int(a) * (16**(maxExp -i))
        decNum+=inter
        i +=1
        a = 0
    return decNum
def decToSeven(l):
    if l == 0:
        return 0 
    i = 0
    s = ("")
    while l > 0:
        i = l%7
        l = l//7
        a = str(i)
        s += a
    return (s[::-1])
def hexToSev(itsMyNum):
    return decToSeven(hextodec(itsMyNum))
###
while True:
    my_num = input("... ")
    print(hexToSev(my_num))
input()





        
