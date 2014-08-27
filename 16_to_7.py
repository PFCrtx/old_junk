def hextodec(x):
    if x == 0:
        decNum = 0
    while True:
        if not str(x).isdigit():
            sign = " "
            x = list(x)
            if any((sign < "A" or sign > "F") and (sign < "0" or sign > "9") for sign in x):
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
            a = ord(a)
            if a >= 65 and a <= 70:
                a = 65 - (55 + (65-a))
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





        
