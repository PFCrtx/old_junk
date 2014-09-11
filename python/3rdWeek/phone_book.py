# --- ! ---
import random
import pickle
amount = int(input("\ "))
alph = list("abcdefghijklmnopqrstuvwxyz")
book = []
name = []
names = set()
i = 0 
numbers = set()
while len(numbers) < amount:
    numbers.add(random.randint(1111111, 9999999))
numbers = list(numbers)
while len(names) < amount:
    while len(name) < (random.randint(4, 10)):
        name.append(alph[random.randint(0, 25)])
    names.add(str("".join(name).capitalize()))
    name = []
names = list(names)
while len(book) < (amount*2):
    book.append(names[i])
    book.append(numbers[i])
    i+=1
f = open("book.txt", "wb")
pickle.dump(book, f)
f.close()
         
        


