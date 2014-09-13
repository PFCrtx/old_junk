def final_test(a, b):
    test = True
    a = list(a)
    b = list(b)
    q = 0
    while q < len(a):
        if a[q] not in b:
            test = False
            break
        q+=1
    return test
#
def normal_ana(my_word):
    arr = []
    select = []
    select_sec = []
    j = 0
    q = 0
    final_arr = []
    gramm = ""
    f = open("di.txt", "r")
    line = f.readline()
    while line:
        if len(line.replace("\n", "")) == len(my_word):
            arr.append(line.replace("\n", ""))
        line = f.readline()
    f.close()
    select += arr
    while j <= (len(my_word)-1):
        for i in select:
            if my_word[j] in i:
                select_sec.append(i)
        j+=1
        select = []
        select += select_sec
        select_sec = []
    while q < len(select):
        gramm = select[q]
        if final_test(gramm, my_word) == True:
            final_arr.append(gramm)
        q+=1
    if len(final_arr) < 1:
        return " Слово отсутствует в словаре. "
    return " ".join(final_arr)         
#
while True:
    ana = input("\...")
    if len(ana) < 2 or (all(n == ana[0] for n in ana)):
        print("Некорректное значение! ")
    print(normal_ana(ana))


        


