import random
alph = list("abcdefghijklmnopqrstuvwxyz")
book = []
name = []
i = 0 # Каждому следующему "имени" - i+1-й номер телефона!
numbers = []
while len(numbers) <= 100001:
    x = random.randint(1111111, 9999999)
    if not x in numbers: #Все номера уникальны.
        numbers.append(x)
while len(book) < 100000:
    while len(name) < (random.randint(4, 10)):
        name.append(alph[random.randint(0, 25)])
    name.append(" - ")
    name.append(str(numbers[i]))
    i+=1     
    book.append("".join(name).capitalize())
    name = [] # Обнуляем "имя".
book = str(book).replace("'", "").replace("[","").replace("]","").replace(",","\n")
f = open("book.txt", "w")
f.write(book)
f.close()
         
        


