def fibo(x):
    a = 0
    b = 1
    i = 1 #Или i = 0, если числа Фибоначчи считать 0, 1, 1, 2, 3 ...
    while i <= x:
        a = a+b
        b = a-b
        i+=1
    return a
#
def fibo_(x): #Выводит все числа Фибоначчи от 0 до x.
    a = 0
    b = 1
    while a <= x:
        print(a)
        a = a+b
        b = a-b
    return ""
#
x = int(input("\ "))
how = input("f1 or f2? ")
if how == "f1":
    print(fibo(x))
elif how == "f2":
    print(fibo_(x))
