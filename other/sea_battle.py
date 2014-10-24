from random import randint
class Area():
    var = ["empty", "set", "dead", "checked"]
    grid = []
    used = []
    def __init__(self, number):
        self.status = "empty"
        self.number = number
        Area.grid.append(self)

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

    def hit_or_kill(q, arr):
        if arr == "Player":
            if q in me.four_funnel:
                me.four_funnel.remove(q)
                if len(me.four_funnel) < 1:
                    return "kill0"
                elif len(me.four_funnel) >= 1:
                    return "hit"
            elif q in me.three_funnel_one:
                me.three_funnel_one.remove(q)
                if len(me.three_funnel_one) < 1:
                    return "kill1"
                elif len(me.three_funnel_one) >= 1:
                    return "hit"
            elif q in me.three_funnel_two:
                me.three_funnel_two.remove(q)
                if len(me.three_funnel_two) < 1:
                    return "kill2"
                elif len(me.three_funnel_two) >= 1:
                    return "hit"
            elif q in me.two_funnel_one:
                me.two_funnel_one.remove(q)
                if len(me.two_funnel_one) < 1:
                    return "kill3"
                elif len(me.two_funnel_one) >= 1:
                    return "hit"
            elif q in me.two_funnel_two:
                me.two_funnel_two.remove(q)
                if len(me.two_funnel_two) < 1:
                    return "kill4"
                elif len(me.two_funnel_two) >= 1:
                    return "hit"
            elif q in me.two_funnel_three:
                me.two_funnel_three.remove(q)
                if len(me.two_funnel_three) < 1:
                    return "kill5"
                elif len(me.two_funnel_three) >= 1:
                    return "hit"
            elif q in me.one_funnel_one:
                return "kill6"
            elif q in me.one_funnel_two:
                return "kill7"
            elif q in me.one_funnel_three:
                return "kill8"
            elif q in me.one_funnel_four:
                return "kill9"
        elif arr == "Enemy":
            if q in you.four_funnel:
                you.four_funnel.remove(q)
                if len(you.four_funnel) < 1:
                    return "kill"
                elif len(you.four_funnel) >= 1:
                    return "hit"
            elif q in you.three_funnel_one:
                you.three_funnel_one.remove(q)
                if len(you.three_funnel_one) < 1:
                    return "kill"
                elif len(you.three_funnel_one) >= 1:
                    return "hit"
            elif q in you.three_funnel_two:
                you.three_funnel_two.remove(q)
                if len(you.three_funnel_two) < 1:
                    return "kill"
                elif len(you.three_funnel_two) >= 1:
                    return "hit"
            elif q in you.two_funnel_one:
                you.two_funnel_one.remove(q)
                if len(you.two_funnel_one) < 1:
                    return "kill"
                elif len(you.two_funnel_one) >= 1:
                    return "hit"
            elif q in you.two_funnel_two:
                you.two_funnel_two.remove(q)
                if len(you.two_funnel_two) < 1:
                    return "kill"
                elif len(you.two_funnel_two) >= 1:
                    return "hit"
            elif q in you.two_funnel_three:
                you.two_funnel_three.remove(q)
                if len(you.two_funnel_three) < 1:
                    return "kill"
                elif len(you.two_funnel_three) >= 1:
                    return "hit"
            elif q in you.one_funnel_one or q in you.one_funnel_two or q in you.one_funnel_three or q in you.one_funnel_four:
                return "kill"
    hit_or_kill = staticmethod(hit_or_kill)

    def create_my_fleet(my_list):
        blueprint = MyFleet.get_fleet()
        if my_list == "Player":
            me.four_funnel += blueprint[0]
            me.tone += blueprint[0]
            me.three_funnel_one += blueprint[1]
            me.ttwo += blueprint[1]
            me.three_funnel_two += blueprint[2]
            me.tthree += blueprint[2]
            me.two_funnel_one += blueprint[3]
            me.tfour += blueprint[3]
            me.two_funnel_two += blueprint[4]
            me.tfive += blueprint[4]
            me.two_funnel_three += blueprint[5]
            me.tsix += blueprint[5]
            me.one_funnel_one += blueprint[6]
            me.tseven += blueprint[6]
            me.one_funnel_two += blueprint[7]
            me.teight += blueprint[7]
            me.one_funnel_three += blueprint[8]
            me.tnine += blueprint[8]
            me.one_funnel_four += blueprint[9]
            me.tten += blueprint[9]
        elif my_list == "Enemy":
            you.four_funnel += blueprint[0]
            you.three_funnel_one += blueprint[1]
            you.three_funnel_two += blueprint[2]
            you.two_funnel_one += blueprint[3]
            you.two_funnel_two += blueprint[4]
            you.two_funnel_three += blueprint[5]
            you.one_funnel_one += blueprint[6]
            you.one_funnel_two += blueprint[7]
            you.one_funnel_three += blueprint[8]
            you.one_funnel_four += blueprint[9]
        elif my_list == 1:
            blueprint = Player.manually
            me.four_funnel += blueprint[0]
            me.tone += blueprint[0]
            me.three_funnel_one += blueprint[1]
            me.ttwo += blueprint[1]
            me.three_funnel_two += blueprint[2]
            me.tthree += blueprint[2]
            me.two_funnel_one += blueprint[3]
            me.tfour += blueprint[3]
            me.two_funnel_two += blueprint[4]
            me.tfive += blueprint[4]
            me.two_funnel_three += blueprint[5]
            me.tsix += blueprint[5]
            me.one_funnel_one += blueprint[6]
            me.tseven += blueprint[6]
            me.one_funnel_two += blueprint[7]
            me.teight += blueprint[7]
            me.one_funnel_three += blueprint[8]
            me.tnine += blueprint[8]
            me.one_funnel_four += blueprint[9]
            me.tten += blueprint[9]
            
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
class Player(Area):
    manually = []
    test = []
    funnels = 20
    my_grid = []
    four_funnel = []
    tone = []
    three_funnel_one = []
    ttwo = []
    three_funnel_two = []
    tthree = []
    two_funnel_one = []
    tfour = []
    two_funnel_two = []
    tfive = []
    two_funnel_three = []
    tsix = []
    one_funnel_one = []
    tseven = []
    one_funnel_two = []
    teight = []
    one_funnel_three = []
    tnine = []
    one_funnel_four = []
    tten = []
    
    def __init__(self):
        pass

    def fire(self, target):
        if not target in Player.test:
            Player.test.append(target)
            self.target = target
            x = Enemy.enemy_grid[target].show_status()
            if x == "set":
                Enemy.funnels -=1
                Enemy.enemy_grid[target].kill_self()
                test = Area.hit_or_kill(target, "Enemy")
                if test == "hit":
                    print(" ")
                    print("Попадание!" + "\n")
                elif test[:4] == "kill":
                    print(" ")
                    print("Неприятельский корабль уничтожен! ")
            elif x == "empty":
                Enemy.enemy_grid[target].mark_self()
                print(" ")
                print("Мимо." + "\n")
                you.ai_fire()
        else:
            print("Некорректные координаты")

class Enemy(Area):

    funnels = 20
    enemy_grid = []
    check = []
    current_target = []

    four_funnel = []
    three_funnel_one = []
    three_funnel_two = []
    two_funnel_one = []
    two_funnel_two = []
    two_funnel_three = []
    one_funnel_one = []
    one_funnel_two = []
    one_funnel_three = []
    one_funnel_four = []

    def __init__(self):
        pass

    def ai_fire(self):
        try: 
            if len(Enemy.current_target) < 1:
                while True:
                    if Player.funnels < 1:
                        break
                    target = randint(0, 99)
                    if not target in Enemy.check:
                        Enemy.check.append(target)
                        break
                x = Player.my_grid[target].show_status()
                if x == "set":
                    Player.funnels -=1
                    Player.my_grid[target].kill_self()
                    m = Enemy.target_silhouette(str(target).split(" "))
                    for i in m:
                        Enemy.check.append(int(i))
                    print("Противник попал по " + re_trans(target))
                    z = Enemy.aim_silhouette(str(target).split(" "))
                    for i in z:
                        Enemy.current_target.append(i)
                    test = Area.hit_or_kill(target, "Player")
                    if test[:4] == "kill":
                        Enemy.current_target.clear()
                        Enemy.dead_silhouette(test[-1:])
                        you.ai_fire()
                    elif test == "hit":
                        you.ai_fire()
                elif x == "empty":
                    print("Противник стреляет по  " + re_trans(target))
            elif len(Enemy.current_target) >=1:
                while True:
                    if Player.funnels < 1:
                        break
                    i = randint(0, len(Enemy.current_target)-1)
                    target = Enemy.current_target[i]
                    if not target in Enemy.check:
                        Enemy.check.append(target)
                        break
                x = Player.my_grid[target].show_status()
                if x == "set":
                    Player.funnels -=1
                    Player.my_grid[target].kill_self()
                    m = Enemy.target_silhouette(str(target).split(" "))
                    for i in m:
                        Enemy.check.append(int(i))
                    print("Противник попал по " + re_trans(target))
                    z = Enemy.aim_silhouette(str(target).split(" "))
                    for i in z:
                        Enemy.current_target.append(i)
                    test = Area.hit_or_kill(target, "Player")
                    if test[:4] == "kill":
                        Enemy.current_target.clear()
                        Enemy.dead_silhouette(test[-1:])
                        you.ai_fire()
                    elif test == "hit":
                        you.ai_fire()
                elif x == "empty":
                    print("Противник стреляет по  " + re_trans(target))
        except UnboundLocalError:
            pass
        
    def aim_silhouette(my_arr):
        re = []
        for elem in my_arr:
            if len(str(elem)) < 2:
                elem = "0" + str(elem)
            if 11 <= int(elem) <= 89 and str(elem)[1] != "9" and int(elem)%10 != 0:
                re.append(int(elem) -10)
                re.append(int(elem) +1)
                re.append(int(elem) +10)
                re.append(int(elem) -1)
            elif int(elem) != 0 and int(elem) != 90 and int(elem)%10 == 0:
                re.append(int(elem) -10)
                re.append(int(elem) +1)
                re.append(int(elem) +10)
            elif  int(elem) != 9 and int(elem) != 99 and str(elem)[1] == "9":
                re.append(int(elem) -10)
                re.append(int(elem) +10)
                re.append(int(elem) -1)
            elif 1 <= int(elem) <= 8:
                re.append(int(elem) -1)
                re.append(int(elem) +1)
                re.append(int(elem) +10)
            elif 91 <= int(elem) <= 98:
                re.append(int(elem) -1)
                re.append(int(elem) +1)
                re.append(int(elem) -10)
            elif int(elem) == 0:
                re.append(int(elem) +1)
                re.append(int(elem) +11)
            elif int(elem) == 9:
                re.append(8)
                re.append(19)
            elif int(elem) == 90:
                re.append(80)
                re.append(91)
                MyFleet.used.append(91)
            elif int(elem) == 99:
                re.append(98)
                re.append(89)
        return re
    aim_silhouette = staticmethod(aim_silhouette)

    def target_silhouette(my_arr):
        re = []
        for elem in my_arr:
            if len(str(elem)) < 2:
                elem = "0" + str(elem)
            if 11 <= int(elem) <= 89 and str(elem)[1] != "9" and int(elem)%10 != 0:
                re.append(int(elem) -11)
                re.append(int(elem) +11)
                re.append(int(elem) +9)
                re.append(int(elem) -9)
            elif int(elem) != 0 and int(elem) != 90 and int(elem)%10 == 0:
                re.append(int(elem) +11)
                re.append(int(elem) -9)
            elif  int(elem) != 9 and int(elem) != 99 and str(elem)[1] == "9":
                re.append(int(elem) -11)
                re.append(int(elem) +9)
            elif 1 <= int(elem) <= 8:
                re.append(int(elem) +9)
                re.append(int(elem) +11)
            elif 91 <= int(elem) <= 98:
                re.append(int(elem) -11)
                re.append(int(elem) -9)
            elif int(elem) == 0:
                re.append(11)
            elif int(elem) == 9:
                re.append(18)
            elif int(elem) == 90:
                re.append(81)
                MyFleet.used.append(91)
            elif int(elem) == 99:
                re.append(88)
        return re
    target_silhouette = staticmethod(target_silhouette)

    def dead_silhouette(n):
        if n == "0":
            qwe = Enemy.aim_silhouette(Player.tone)
            rty = Enemy.target_silhouette(Player.tone)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
                    
        elif n == "1":
            qwe = Enemy.aim_silhouette(Player.ttwo)
            rty = Enemy.target_silhouette(Player.ttwo)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "2":
            qwe = Enemy.aim_silhouette(Player.tthree)
            rty = Enemy.target_silhouette(Player.tthree)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "3":
            qwe = Enemy.aim_silhouette(Player.tfour)
            rty = Enemy.target_silhouette(Player.tfour)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "4":
            qwe = Enemy.aim_silhouette(Player.tfive)
            rty = Enemy.target_silhouette(Player.tfive)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "5":
            qwe = Enemy.aim_silhouette(Player.tsix)
            rty = Enemy.target_silhouette(Player.tsix)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "6":
            qwe = Enemy.aim_silhouette(Player.tseven)
            rty = Enemy.target_silhouette(Player.tseven)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "7":
            qwe = Enemy.aim_silhouette(Player.teight)
            rty = Enemy.target_silhouette(Player.teight)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "8":
            qwe = Enemy.aim_silhouette(Player.tnine)
            rty = Enemy.target_silhouette(Player.tnine)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
        elif n == "9":
            qwe = Enemy.aim_silhouette(Player.tten)
            rty = Enemy.target_silhouette(Player.tten)
            for i in qwe:
                if not i in Enemy.check:
                    Enemy.check.append(i)
            for i in rty:
                if not i in rty:
                    Enemy.check.append(i)
                    
    dead_silhouette = staticmethod(dead_silhouette)
    
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
    
###

def my_silhouette(my_arr):
    re = []
    ree = set()
    for elem in my_arr:
        if len(str(elem)) < 2:
            elem = "0" + str(elem)
        if 11 <= int(elem) <= 89 and str(elem)[1] != "9" and int(elem)%10 != 0:
            re.append(int(elem) -10)
            re.append(int(elem) +1)
            re.append(int(elem) +10)
            re.append(int(elem) -1)
            re.append(int(elem) -11)
            re.append(int(elem) +11)
            re.append(int(elem) +9)
            re.append(int(elem) -9)
        elif int(elem) != 0 and int(elem) != 90 and int(elem)%10 == 0:
            re.append(int(elem) -10)
            re.append(int(elem) +1)
            re.append(int(elem) +10)
            re.append(int(elem) +11)
            re.append(int(elem) -9)        
        elif  int(elem) != 9 and int(elem) != 99 and str(elem)[1] == "9":
            re.append(int(elem) -10)
            re.append(int(elem) +10)
            re.append(int(elem) -1)
            re.append(int(elem) -11)
            re.append(int(elem) +9)
        elif 1 <= int(elem) <= 8:
            re.append(int(elem) -1)
            re.append(int(elem) +1)
            re.append(int(elem) +10)
            re.append(int(elem) +9)
            re.append(int(elem) +11)
        elif 91 <= int(elem) <= 98:
            re.append(int(elem) -1)
            re.append(int(elem) +1)
            re.append(int(elem) -10)
            re.append(int(elem) -11)
            re.append(int(elem) -9)
        elif int(elem) == 0:
            re.append(int(elem) +1)
            re.append(int(elem) +11)
            re.append(10)
        elif int(elem) == 9:
            re.append(8)
            re.append(19)
            re.append(18)
        elif int(elem) == 90:
            re.append(80)
            re.append(81)
            re.append(91)
        elif int(elem) == 99:
            re.append(98)
            re.append(89)
            re.append(88)
        k = 0
        while True:
            k = 0
            for i in re:
                if i in my_arr:
                    re.remove(i)
                    k+=1
            if k == 0:
                break
        for i in re:
            ree.add(i)
    return list(ree)

def final_test(arr):
    test = []
    sn = 0
    st = 0
    for elem in arr:
        test.append(elem)
    t = sorted(test)
    try:
        for i in t:
            if t[(t.index(i))+1] - i == 1:
                sn +=0
            else:
                sn += 1
    except IndexError:
        pass
    try:
        for i in t:
            if t[(t.index(i))+1] - i == 10:
                st +=0
            else:
                st += 1
    except IndexError:
        pass
    if sn > 0 and st > 0:
        return False
    else:
        return True

def usefull(arr):
    test = []
    sign = 0
    for i in arr:
        test += my_silhouette(i)
    for i in arr:
        for elem in i:
            if elem in test:
                sign += 1
    if sign == 0:
        return True
    elif sign > 0:
        return False

def allow(arr):
    allow = 0
    if usefull(arr) == True:
        allow += 1
    for elem in arr:
        if final_test(elem) == True:
            allow += 1
    if allow == 11:
        return True
    else:
        return False

def game_show(my_list, m = 0):
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
        n = my_list[i].show_status()
        if n == "empty":
            s += " : "
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
            if m == 0:
                s += " : "
            elif m == 1:
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
def create_game(n = 0):
    global me
    global you
    if n == 0:
        me = Player()
        Area.create_grid()
        Area.create_my_fleet("Player") 
        Player.my_grid += Area.grid
        Area.grid.clear()
        you = Enemy()
        Area.create_grid()
        Area.create_my_fleet("Enemy")
        Enemy.enemy_grid += Area.grid
        Area.grid.clear()
    elif n == 1:
        me = Player()
        Area.create_grid()
        Area.create_my_fleet(1)
        Player.my_grid += Area.grid
        Area.grid.clear()
        you = Enemy()
        Area.create_grid()
        Area.create_my_fleet("Enemy")
        Enemy.enemy_grid += Area.grid
        Area.grid.clear()
        
def translate(my_coord):
    z = 0
    my_dict = {"a": -1, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "k": 9}
    
    x = my_dict.get(my_coord[0])
    y = int(my_coord[1:])
    if int(my_coord[1:]) == 0 and my_coord[0] == "a":
        z = x + y
    elif int(my_coord[1:]) != 0 and my_coord[0] == "a":
        z = 10*(y-1)
    elif my_coord[0] != "a":
        z = x + (10 *(y-1))
    return z

def re_trans(my_coord):
    my_dict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "k"}
    if 0 <= my_coord <= 9:
        return my_dict.get(my_coord) + "1"
    elif 10 <= my_coord <= 89:
        return my_dict.get(int(str(my_coord)[1])) + str((my_coord//10)+1)
    elif 90 <= my_coord <= 99:
        return my_dict.get(int(str(my_coord)[1])) + "10"

def right_input(s):
    while True:
        if 2 > len(s) or len(s) > 3:
            return False
        else:
            if len(s) == 2:
                if (ord(s[0]) == 107 or (97 <= ord(s[0]) <= 105)) and (49 <= ord(s[1]) <= 57):
                    return True
                else:
                    return False
            elif len(s) == 3:
                if (ord(s[0]) == 107 or (97 <= ord(s[0]) <= 105)) and (49 <= ord(s[1]) <= 57) and (ord(s[2]) == 48):
                    return True
                else:
                    return False
print("Когда уходить с корабля крысе, если она капитан? © ")
print(" ")
print("Чтобы <долго и муторно> расставлять свой флот вручную, введите 's'.")
print(" ")
start = input("Нажмите на Enter, чтобы начать игру... ")
if start != "s":
    create_game()
    print(" ")
    print("Вы:")
    print(" ")
    print(game_show(Player.my_grid, 1))
    print(" ")
    print("Противник:")
    print(" ")
    print(game_show(Enemy.enemy_grid))
elif start == "s":
    j = 1
    print(" a b c d e f g h i k ")
    while j <= 10:
        print(j)
        j+=1
    
    man = [[], [], [], [], [], [], [], [], [], []]
    print("Начните вводить координаты с четырёхпалубного корабля.")
    print("Координаты разделяются одним пробелом (a1 b1 c1 d1). ")
    print(" ")
    i = 1
    k = 0
    arr = []
    while True:
        if i == 1:
            n = 4
        elif 2 <= i <= 3:
            n = 3
        elif 4 <= i <= 6:
            n = 2
        elif 7 <= i <= 10:
            n = 1
        x = input("Введите координаты " + str(i)+ " корабля: ")
        x = x.strip()
        x = x.split(" ")
        if  len(list(filter(lambda x: right_input(x), x))) == n and len(list(filter(lambda x: right_input(x), x))) != False:
            for elem in x:
                arr.append(translate(elem))
            man[k] +=arr
            k+=1
            arr.clear()
            i+=1

        if i > 10:
            if allow(man) == True:
                Player.manually += man
                create_game(1)
                print("Вы:")
                print(" ")
                print(game_show(Player.my_grid, 1))
                print(" ")
                print("Противник:")
                print(" ")
                print(game_show(Enemy.enemy_grid))
                break
            else:
                man = [[], [], [], [], [], [], [], [], [], []]
                i = 1
                k = 0
                arr = []
                print("Не все координаты введены корректно, попробуйте снова.")

while True:
    if Enemy.funnels == 0 or Player.funnels == 0:
        break
    x = input(" Координаты цели: ")
    if x == "q":
        break
    t = right_input(x)
    if t == False:
        continue
        
    elif not x.isdigit():
        x = translate(x)
        me.fire(x)
        if Enemy.funnels == 0 or Player.funnels == 0:
            break
        print(" ")
        print("Вы: ")
        print(" ")
        print(game_show(Player.my_grid, 1))
        print(" ")
        print("Противник: ")
        print(" ")
        print(game_show(Enemy.enemy_grid))
    elif x == "rf":
        Area.grid.clear()
        Area.create_grid()
        Area.create_my_fleet()
        print(game_show(Player.my_grid, 1))

if Player.funnels == 0:
    print("Вы проиграли.")
elif Enemy.funnels == 0:
    print("Победа!")  
    
