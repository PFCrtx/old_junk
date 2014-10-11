from random import randint
class Player():
    
    defense = ["A", "B", "C", "D"]
    ring = []
    
    def __init__(self, name):
        self.name = name
        self.block = "B"
        self.health = 6

    def show_block(self):
        return self.block

    def show_health(self):
        return self.health

    def change_block(self, new_block):
        if new_block in Player.defense:
            self.block = new_block
            print("OK")
        else:
            pass

    def hit(self, target, aim):

        if 6 > int(aim) > 0:

            if aim == 1 and target.block == "A":
                print("Ваш удар блокирован.")
                target.change_block()
            elif aim == 1 and target.block != "A":
                target.health -= 1
                print("Вы нанесли удар!")
                if target.health <= 0:
                    print(target.name + " нокаутирован! Бой завершен.")
                else:
                    target.change_block()
            elif aim == 2 and (target.block == "A" or target.block == "B"):
                print("Ваш удар блокирован.")
                target.change_block()
            elif aim == 2 and target.block != "A" and target.block != "B":
                target.health -= 1
                print("Вы нанесли удар!")
                if target.health <= 0:
                    print(target.name + " нокаутирован! Бой завершен.")
                else:
                    target.change_block()
            elif aim == 3 and (target.block == "B" or target.block == "C"):
                print("Ваш удар блокирован.")
                target.change_block()
            elif aim == 3 and target.block != "B" and target.block != "C":
                target.health -= 1
                print("Вы нанесли удар!")
                if target.health <= 0:
                    print(target.name + " нокаутирован! Бой завершен.")
                else:
                    target.change_block()
            elif aim == 4 and (target.block == "C" or target.block == "D"):
                print("Ваш удар блокирован.")
                target.change_block()
            elif aim == 4 and target.block != "C" and target.block != "D":
                target.health -= 1
                print("Вы нанесли удар!")
                if target.health <= 0:
                    print(target.name + " нокаутирован! Бой завершен.")
                else:
                    target.change_block()
            elif aim == 5 and target.block == "D":
                print("Ваш удар блокирован.")
                target.change_block()
            elif aim == 5 and target.block != "D":
                target.health -= 1
                print("Вы нанесли удар!")
                if target.health <= 0:
                    print(target.name + " нокаутирован! Бой завершен.")
                else:
                    target.change_block()
        else:
            pass

class Enemy(Player):

    def change_block(self):
        self.block = Player.defense[randint(0, 3)]
        Player.ring[1].hit()

    def hit(self, target = "", aim = ""):
        target = Player.ring[0]
        aim = randint(1, 5)
        if aim == 1 and target.block == "A":
            print("Вы блокировали удар.")
        elif aim == 1 and target.block != "A":
            target.health -= 1
            print("Вам нанесён удар!")
            if target.health <= 0:
                print(target.name + " нокаутирован! Бой завершен.")
            else:
                pass
        elif aim == 2 and (target.block == "A" or target.block == "B"):
            print("Вы блокировали удар.")
        elif aim == 2 and target.block != "A" and target.block != "B":
            target.health -= 1
            print("Вам нанесён удар!")
            if target.health <= 0:
                print(target.name + " нокаутирован! Бой завершен.")
            else:
                pass
        elif aim == 3 and (target.block == "B" or target.block == "C"):
            print("Вы блокировали удар.")
        elif aim == 3 and target.block != "B" and target.block != "C":
            target.health -= 1
            print("Вам нанесён удар!")
            if target.health <= 0:
                print(target.name + " нокаутирован! Бой завершен.")
            else:
                pass
        elif aim == 4 and (target.block == "C" or target.block == "D"):
            print("Вы блокировали удар.")
        elif aim == 4 and target.block != "C" and target.block != "D":
            target.health -= 1
            print("Вам нанесён удар!")
            if target.health <= 0:
                print(target.name + " нокаутирован! Бой завершен.")
            else:
                pass
        elif aim == 5 and target.block == "D":
            print("Вы блокировали удар.")
        elif aim == 5 and target.block != "D":
            target.health -= 1
            print("Вам нанесён удар!")
            if target.health <= 0:
                print(target.name + " нокаутирован! Бой завершен.")
            else:
                pass

#
name = input("\Введите ваше имя: ")
ename = input("\Введите имя противника: ")
if name == "":
    name = "Tyler"
if ename == "":
    ename = "Cornelius"
    
me = Player(name)
Player.ring.append(me)
you = Enemy(ename)
Player.ring.append(you)
k = 1
print("Чтобы выбрать зону атаки, введите число от 1 до 5. ")
print("Чтобы изменить зону защиты, введите 'A', 'B', 'C' или 'D': ")
while True:
    p = me.show_health()
    q = you.show_health()
    if p <= 0:
        print("Вы проиграли.")
        break
    if  q <= 0:
        print("Вы победили!")
        break
    
    print("Раунд " + str(k))
    x = input("CO! " )
    if not x.isdigit():
        if x == "A":
            me.change_block("A")
        elif x == "B":
            me.change_block("B")
        elif x == "C":
            me.change_block("C")
        elif x == "D":
            me.change_block("D")
    if x.isdigit():
        x = int(x)
        if x == 1:
            me.hit(you, 1)
            k+=1
        elif x == 2:
            me.hit(you, 2)
            k+=1
        elif x == 3:
            me.hit(you, 3)
            k+=1
        elif x == 4:
            me.hit(you, 4)
            k+=1
        elif x == 5:
            me.hit(you, 5)
            k+=1
        
            
        

