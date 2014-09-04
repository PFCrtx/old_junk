def is_number(x):
    """ Является ли 'x' вещественным десятичным числом."""
    x = list(x)
    i = "" # Для "склеивания" в сплошную строку содержимого списка.
    test = 0
    if any((ord(n) < 45 or ord(n) > 46) and (ord(n) < 48 or ord(n) > 57) for n in x):
        test = 1
    elif "-" in x and (x.count("-") > 1 or x.index("-") != 0 or ("." in x and x.index(".") == 1)):
        test = 2
    elif "." in x and (x.count(".") > 1 or x.index(".") == 0 or x.index(".") == (len(x)-1)):
        test = 3
    elif "0" in x and len(x) > 1 and x[0] == "0" and x[1] != ".":
        test = 4
    elif "0" in x and len(x) > 2 and x[0] == "-" and x[1] == "0" and x[2] != ".":
        test = 5
    elif len(x) > 1 and all(n == "0" or n == "-" or n == "." for n in x):
        test = 6
    elif len(x) == 1 and x[0] == "-":
        test = 7
    else:
        test = 0
    if test == 0:
#   print(i.join(x))
        return True
    elif test > 0:
        return False
#######################
while True:
    x = input("\ ")
    if is_number(x):
        print(x)
