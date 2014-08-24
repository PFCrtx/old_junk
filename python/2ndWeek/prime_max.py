def prime(x):
    i = 2
    j = 0
    while ((i*i) <= x) and (j != 1):
        if x%i == 0:
            j = 1
        else:
            i+=1
    if j == 1:
        return 0
    else:
        return x
#
def max_prime(x):
    if prime(x) == x:
        return x
    else:
        y = x - 1
        while y > 1:
            if prime(y) == y and x%y == 0:
                return y
                break
            else:
                y-=1
#####
while True:
    x = int(input(" "))
    print(max_prime(x))


        


      
    
