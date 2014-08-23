def input_int(a, b):
    x = input(" ")
    while True:
        if not x.isdigit() or ((a > int(x)) or (int(x) > b)):
            x = input("wrong ")
        else:
            break
    return x
#####
qwe = int(input(" "))
rty = int(input(" "))          
x = input_int(qwe, rty)
print(x)
#####

