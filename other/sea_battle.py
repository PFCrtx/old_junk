#
from random import randint
class Area():
    var = ["empty", "set", "dead", "checked"]
    grid = []
    funnels = 0
    used = []

    def __init__(self, number):
        self.status = "empty"
        self.number = number
        Area.grid.append(self) # Можно пропустить эту строчку, добавив в create_grid "Area.grid.append(a)". Как лучше?

    def show_status(self):
        return self.status

    def set_funnel(self):
        if self.status == "empty":
            self.status = "set"

    def mark_self(self):
        if self.status == "empty":
            self.status = "checked"

    def kill_self(self):
        if self.status == "set":
            self.status = "dead"

    def create_my_fleet():
        blueprint = MyFleet.get_fleet()
        for elem in blueprint:
            for i in elem:
                if len(str(i)) < 2:
                    i = "0" + str(i)
                Area.grid[int(i)].set_funnel()
        
    create_my_fleet = staticmethod(create_my_fleet)
    

    def create_grid():
        i = 0
        while i <= 99:
            a = Area(i)
            i+=1
    create_grid = staticmethod(create_grid)
#
class Player():
    def __init__(self):
        pass

    def fire(self, target):
        self.target = target
        x = Area.grid[target].show_status()
        if x == "set":
            Area.grid[target].kill_self()
            print("Попадание!" + "\n")
        elif x == "empty":
            Area.grid[target].mark_self()
            print("Мимо." + "\n")
            
            

    
class MyFleet():
    
    used = []
    
    def create_ship(x):
        while True:
            test = 0
            arr = []
            direct = randint(0, 1)
            if direct == 0:
                while True:
                    if len(arr) >= x:
                        break
                    n = str(randint(0, 99))
                    if len(n) < 2:
                        n = "0" + n
                    if int(n[1]) > (10-x):
                        continue
                    else:
                        arr.append(int(n))
                        while len(arr) < x:
                            n = int(n)
                            n+=1
                            arr.append(n)
            elif direct == 1:
                n = randint(0, (109-(10*x)))
                arr.append(n)
                while len(arr) < x:
                    n +=10
                    arr.append(n)

            for elem in arr:
                if elem in MyFleet.used:
                    test+=1
            if test == 0:
                for elem in arr:
                    MyFleet.used.append(elem)
                break
        return arr

    create_ship = staticmethod(create_ship)

    def silhouette(my_arr):
        for elem in my_arr:
            if len(str(elem)) < 2:
                elem = "0" + str(elem)
            if 11 <= int(elem) <= 89 and str(elem)[1] != "9" and elem%10 != 0:
                MyFleet.used.append(int(elem) -10)
                MyFleet.used.append(int(elem) -9)
                MyFleet.used.append(int(elem) +1)
                MyFleet.used.append(int(elem) +11)
                MyFleet.used.append(int(elem) +10)
                MyFleet.used.append(int(elem) +9)
                MyFleet.used.append(int(elem) -11)
                MyFleet.used.append(int(elem) -1)
            elif int(elem) != 0 and int(elem) != 90 and int(elem)%10 == 0:
                MyFleet.used.append(int(elem) -10)
                MyFleet.used.append(int(elem) -9)
                MyFleet.used.append(int(elem) +1)
                MyFleet.used.append(int(elem) +11)
                MyFleet.used.append(int(elem) +10)
            elif  int(elem) != 9 and int(elem) != 99 and str(elem)[1] == "9":
                MyFleet.used.append(int(elem) -10)
                MyFleet.used.append(int(elem) +10)
                MyFleet.used.append(int(elem) +9)
                MyFleet.used.append(int(elem) -11)
                MyFleet.used.append(int(elem) -1)
            elif 1 <= int(elem) <= 8:
                MyFleet.used.append(int(elem) -1)
                MyFleet.used.append(int(elem) +1)
                MyFleet.used.append(int(elem) +11)
                MyFleet.used.append(int(elem) +9)
                MyFleet.used.append(int(elem) +10)
            elif 91 <= int(elem) <= 98:
                MyFleet.used.append(int(elem) -1)
                MyFleet.used.append(int(elem) +1)
                MyFleet.used.append(int(elem) -10)
                MyFleet.used.append(int(elem) -9)
                MyFleet.used.append(int(elem) -11)
            elif int(elem) == 0:
                MyFleet.used.append(int(elem) +1)
                MyFleet.used.append(int(elem) +10)
                MyFleet.used.append(int(elem) +11)
            elif int(elem) == 9:
                MyFleet.used.append(8)
                MyFleet.used.append(18)
                MyFleet.used.append(19)
            elif int(elem) == 90:
                MyFleet.used.append(80)
                MyFleet.used.append(81)
                MyFleet.used.append(91)
            elif int(elem) == 99:
                MyFleet.used.append(98)
                MyFleet.used.append(88)
                MyFleet.used.append(89)
    silhouette = staticmethod(silhouette)

    def get_fleet():
        my_fleet = []
        
        ship = MyFleet.create_ship(4)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(3)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(3)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(2)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(2)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(2)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(1)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(1)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(1)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        ship = MyFleet.create_ship(1)
        MyFleet.silhouette(ship)
        my_fleet.append(ship)
        MyFleet.used.clear()
        return my_fleet

    get_fleet = staticmethod(get_fleet)
    
###########
def test_show():
    i = 0
    s = "1  "
    test = 0
    j = 1
    while i <= 99:
        if i > 99:
            test = 0
        if test == 0:
            print("    a  b  c  d  e  f  g  h  i  k ")
            print(" ")
            test+=1
        n = Area.grid[i].show_status()
        if n == "empty":
            s += " o "
            i+=1
            if len(s) == 33:
                s+="\n"
                print(s)
                j+=1
                if len(str(j)) > 1:
                    s = str(j) + " "
                elif len(str(j)) == 1:
                    s = str(j) + "  "
        elif n == "set":
            s += " F "
            i+=1
            if len(s) == 33:
                s+="\n"
                print(s)
                j+=1
                if len(str(j)) > 1:
                    s = str(j) + " "
                elif len(str(j)) == 1:
                    s = str(j) + "  "
        elif n == "dead":
            s += " X "
            i+=1
            if len(s) == 33:
                s+="\n"
                print(s)
                j+=1
                if len(str(j)) > 1:
                    s = str(j) + " "
                elif len(str(j)) == 1:
                    s = str(j) + "  "
        elif n == "checked":
            s += " N "
            i+=1
            if len(s) == 33:
                s+="\n"
                print(s)
                j+=1
                if len(str(j)) > 1:
                    s = str(j) + " "
                elif len(str(j)) == 1:
                    s = str(j) + "  "
    return " "
#
me = Player()
Area.create_grid()
Area.create_my_fleet()
while True:
    x = input("\ ")
    if x == "t":
        print(test_show())
    elif x.isdigit():
        if len(x) < 2:
            x = "0" + x
        me.fire(int(x))
        print(test_show())
    elif x == "q":
        break
#i = 0
#s = ""

        

    


        
        
    
