import random
import pickle
import bisect
import time
def get_phone_book(amount):
    """Генерирует файл с телефонной книгой численностью в amount абонентов и файл со строковой версией книги (my_book.txt)"""
    name = []
    names = set()
    alph = list("abcdefghijklmnopqrstuvwxyz")
    letter = ""
    number = 0
    numbers = set()
    book = []
    i = 0
    while len(names) < amount:
        while len(name) < (random.randint(4, 10)):
            letter = alph[random.randint(0, 25)]
            name.append(letter)
        name = str("".join(name)).capitalize()
        names.add(name)
        name = []
    while len(numbers) < amount:
        number = random.randint(1111111, 9999999)
        numbers.add(number)
    names = list(names)
    numbers = list(numbers)
    while len(book) < (amount*2):
        book.append(names[i])
        book.append(numbers[i])
        i+=1
    f = open("book.txt", "wb")
    pickle.dump(book, f)
    f.close()
    f = open("my_book.txt", "w")
    f.write(str(book).replace(",", "\n").replace("[", "").replace("]", ""))
    f.close()
#
def book_to_dict():
    """Считывает книгу в словарь """
    f = open("book.txt", "rb")
    a = pickle.load(f)
    f.close()
    dic = {}
    i = 1
    while len(dic) <= ((len(a)/2)-1):
        dic[a[i]] = a[i-1]
        i+=2
    return dic
#
def book_to_tuple():
    """ Считывает книгу в список кортежей"""
    my_list = []
    i = 0
    f = open("book.txt", "rb")
    x = pickle.load(f)
    f.close()
    while len(my_list) <= (((len(x))/2)-1):
        my_tup = (x[i], x[i+1])
        my_list.append(my_tup)
        my_tup = ()
        i+=2
    return my_list
#
def sorted_list():
    """ Считывает книгу в упорядоченный список кортежей """
    my_list = []
    i = 1
    f = open("book.txt", "rb")
    x = pickle.load(f)
    f.close()
    while len(my_list) <= (((len(x))/2)-1):
        my_tup = (x[i], x[i-1])
        my_list.append(my_tup)
        my_tup = ()
        i+=2
    my_list = sorted(my_list)
    return my_list
#
def search_dict(out, search_n):
    """ Поиск по словарю """
    if out.get(search_n) == None:
        return("Error")
    else:
        return out.get(search_n)
#
def search_list(out, search_n):
    """ Поиск по списку кортежей """
    j = 0
    name = 0
    while j < len(out):
        if search_n in out[j]:
            name = out[j]
            break
        else:
            j+=1
    if name == 0:
        return "Error"
    else:
        return name[0]
#
def search_sort(out, search_n):
    """ Поиск по упорядоченному списку кортежей """
    keys = [i[0] for i in out]
    bi = out[bisect.bisect_left(keys, search_n)]
    if not search_n in keys:
        return "Error"
    else:
        return bi[1]
#
def speed(foo, test):
    """ Сто раз ищет принятой функцией <корректное, но заведомо отсутствующее> значение в соответствующем списке; возвращает частное от деления 10 на затраченное время """
    k = 0
    while k <=100:
        t = time.clock()
        foo(out, test)
        k+=1
    return 10/t
##
my_amount = int(input("\Введите кол-во абонентов: "))
get_phone_book(my_amount)
search_n = 0
print("Введите 1, чтобы прочитать телефонную книгу в словарь ")
print("Введите 2, чтобы прочитать телефонную книгу в список кортежей ")
print("Введите 3, чтобы прочитать телефонную книгу в упорядоченный список кортежей ")
choice = int(input("\ "))
if choice == 1:
    out = book_to_dict()
elif choice == 2:
    out = book_to_tuple()
elif choice == 3:
    out = sorted_list()
print("OK")
while True:
    search_n = int(input("Введите номер: "))
    if search_n == 999:
        break
    if len(str(search_n)) != 7:
        print("Error")
    elif choice == 1:
        print(search_dict(out, search_n))
        print("Введите 999, чтобы получить оценку эффективности поиска")
    elif choice == 2:
        print(search_list(out, search_n))
        print("Введите 999, чтобы получить оценку эффективности поиска")
    elif choice == 3:
        print(search_sort(out, search_n))
        print("Введите 999, чтобы получить оценку эффективности поиска")
if choice == 1:
    print(speed(search_dict, 1000001))
elif choice == 2:
    print(speed(search_list, 1000001))
elif choice == 3:
    print(speed(search_sort, 1000001))
input()
#####
