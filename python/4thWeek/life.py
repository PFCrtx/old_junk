class Cell():
    
    status = ["dead", "alive"]

    population = []
    
    def __init__(self, number = 0):
        self.number = number
        self.status = "dead"

    def change_status(self):
        """ Меняет состояние клетки на противоположное"""
        if self.status == "alive":
            self.status = "dead"
        elif self.status == "dead":
            self.status = "alive"

    def show_status(self):
        """ Возвращает текущее остояние клетки """
        return self.status

    def show_number(self):
        """ Возвращает порядковый номер клетки"""
        return self.number

    def check_neighbors(self):
        """ Проверет 8 соседних клеток; определяет на основании проверки статус клетки в следующем поколении."""
        dead_neighbor = 0
        alive_neighbor = 0
        my_number = self.number
        if 11 <= my_number <= 88 and len(str(my_number)) > 1 and my_number%10 != 0 and str(my_number)[1] != "9":
            n = str(self.number + 1)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
            n = str(self.number - 1)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
            n = str(self.number - 10)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
            n = str(self.number + 10)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
            n = str(self.number - 11)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
            n = str(self.number + 11)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
            n = str(self.number - 9)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
            n = str(self.number + 9)
            if len(n) == 1:
                n = "0" + n
            test = Cell.population[int(n[0])][int(n[1])].show_status()
            if test == "alive":
                alive_neighbor +=1
            if test == "dead":
                dead_neighbor +=1
        else:
            if self.status == "alive":
                return "die"
            elif self.status == "dead":
                return "stay"
        if self.status == "dead" and alive_neighbor == 3:
            return "reborn"
        elif self.status == "alive" and alive_neighbor > 3:
            return "die"
        elif self.status == "alive" and 2 <= alive_neighbor <= 3:
            return "stay"
        elif self.status == "alive" and alive_neighbor < 2:
            return "die"
        elif self.status == "dead" and alive_neighbor < 3:
            return "stay"
        elif self.status == "dead" and alive_neighbor > 3:
            return "stay"

    def generation():
        """ Проверяет статус будущего поколения для всех клеток в текущем массиве."""
        q = 0
        n = []
        while q <= 9:
            subn = list(map(lambda x: x.check_neighbors(), Cell.population[q]))
            n.append(subn)
            q+=1

        i = 0
        k = 0
        while k <= 9:
            while i <= 9:
                if n[k][i] == "die":
                    Cell.population[k][i].change_status()
                if n[k][i] == "reborn":
                    Cell.population[k][i].change_status()
                    
                i+=1
            i=0
            k+=1

    generation = staticmethod(generation)

    def create_field():
        """ Создаёт массив из 100 "мёртвых" клеток"""
        i = 0
        arr = []
        while i < 100:
            while len(arr) < 10:
                c = Cell(i)
                arr.append(c)
                i+=1
            Cell.population.append(arr)
            arr = []
            
    create_field = staticmethod(create_field)

    def set_start_position(my_list):
        """Позволяет пользователю задать стартовое состояние поля, меняя состояние отдльных клеток."""
        x = Cell.population
        i = 0
        while i <= len(my_list)-1:
            if len(my_list[i]) < 2:
                   my_list[i] = "0" + my_list[i]
            coord = my_list[i]

            a = int(coord[0])
            b = int(coord[1])
            x[a][b].change_status()
            i+=1

    set_start_position = staticmethod(set_start_position)
#
def life(step):
    """step раз сменяет поколения клеток; иллюстрирует этот процесс в псевдографике"""
    j = 0
    i = 0
    s = ""
    kk = 0
    while kk <= step:
        while j <=9:
            while i <= 9:
                if Cell.population[j][i].show_status() == "dead":
                    y = " O "
                elif Cell.population[j][i].show_status() == "alive":
                    y = " Z "
                i+=1
                s += y
            print(s.center(80))
            j+=1
            i = 0
            s = ""
        print(" ")
        kk+=1
        j=0
        Cell.generation()

#######################################################################
st = ""
for i in range(101):
    if i%10 == 0 and i != 0:
        st+="\n"
        print(st)
        st = " "
    if int(i) <= 9:
        st+=str(i) + "  "
    elif int(i) > 9:
        st+=str(i) + " "
Cell.create_field()
my_list = []
while True:
    my_cell = input("Вводите номера полей с живыми клетками (от 1 до 99) по одному: ")
    if my_cell == "":
        break
    my_list.append(my_cell)
    print("Нажмиет Enter, если все необходимые координаты введены.")
Cell.set_start_position(my_list)
x = int(input("Введите кол-во поколений: "))
print(" ")
life(x)

    
    
    
        


    

    
