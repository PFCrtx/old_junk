def fibo(n):
    print("Начинаю вычислять число Фибоначчи № " + str(n))
    if n == 1: return 1
    if n == 0: return 0
    result = fibo(n - 1) + fibo(n - 2)
    print("Число Фибоначчи № " + str(n) + " = " + str(result))
    return result
#
x = int(input("\ "))
print(fibo(x))
