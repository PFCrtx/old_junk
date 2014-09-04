def sieve(x):
    import math
    arr = []
    i = 2
    p = 2
    j = 0
    while i <= x:
        arr.append(i)
        i+=1
    while p <= math.sqrt(x):
        for n in arr:
            if n != p and n%p == 0:
                arr.remove(n)
        j+=1
        p = arr[j]
    return str(arr).replace("[", "").replace("]", "")
#
x = int(input("\ "))
print(sieve(x))
