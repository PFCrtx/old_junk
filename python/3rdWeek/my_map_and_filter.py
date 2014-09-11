def my_map(foo, my_list):
    it = []
    for i in my_list:
        it.append(foo(i))
    return it
#
arr = [1, 3, 0, 7, 42]
y = lambda x: str(x) + str(x)
#
print(my_map(y, arr))
# Но!
# print(map(y, arr)) - Пишет <map object at 0x00000000036B3A90>
# Корректно работает print(list(map(y, arr)))
def my_filter(foo, my_list):
    it = []
    for i in my_list:
        if foo(i) == True:
            it.append(i)
    return it
#   
def leap_year(x):
    return x%4 == 0 and (x%100 != 0 or x%400 == 0)
#
arr = [1600, 1700, 1800, 1900, 1984, 1995, 2000, 2012, 2014, 2016]
#
print(my_filter(leap_year, arr))

        
