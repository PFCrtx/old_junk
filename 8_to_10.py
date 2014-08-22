def octodec(x):
    dl = len(x) -1
    i = 0
    z = 0
    y = 0
    while i <= dl:
        z = x[i] 
        y += int(z)* (8**(dl - i))
        i+=1
    return y
###
while True:
    qwe = input("... ")
    qwe = octodec(qwe)
    print(qwe)
input()

