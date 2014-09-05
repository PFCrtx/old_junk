import random
generations = []
alph = list(" abcdefghijklmnopqrstuvwxyz")
def rand_str(x):
    """Возвращает рандомную строку из x символов """
    rand_str = []
    while len(rand_str) < len(x):
        rand_str.append(alph[random.randint(0, 26)])
    return str(''.join(rand_str))
#
def compare_strings(a, b):
    """Возвращает кол-во совпадающих в двух строках позиций """
    i = 0
    j = 0
    while i < len(a):
        if a[i] == b[i]:
            j+=1
        i+=1
    return j
#
def mutation(s):
    """Заменяет букву на случайной позиции в строке другой случайной буквой. """
    s = list(s)
    i = random.randint(0, (len(s) -1))
    del s [i]
    s.insert(i, alph[random.randint(0, 26)])
    str(s)
    return "".join(s)
#
my_str = input("\ ").lower()
r_str = rand_str(my_str)
k = 0
while compare_strings(my_str, r_str) == 0:
    r_str = rand_str(my_str)
generations.append(str(k) + ": " + r_str)
while r_str != my_str:
     new_str = mutation(r_str)
     if compare_strings(my_str, new_str) >= compare_strings(my_str, r_str): # Наш "отбор" одобряет и нейтральные мутации, поэтому >=, а не строго >.
         r_str = new_str
         k+=1
         generations.append(str(k) + ": " + r_str)   
done = (str(generations).replace("'", "").replace("[","").replace("]",""))
f = open("evol.txt", "w")
f.write(done)
f.close()




