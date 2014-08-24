def max_prime(x):
    i = 2
    j = 0
    z = 0
    y = x
    while x > 1:
        while ((i*i) <= x + 2) and (j != 1):
            if x == 2:
                z = 2
                break
            if x%i == 0:
                j = 1
            else:
                i+=1
            if j == 0:
                z = x
            else:
                z = 0
        if z == x:
            if y%z == 0:
                return z
                break
        x-=1
        z =0
        i=2
        j=0
###
while True:
    x = int(input("\ "))
    print(max_prime(x))
input()

    







