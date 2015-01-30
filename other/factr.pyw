from tkinter import *

class MyApp(Tk):

    def __init__ (self):
        Tk. __init__ (self)
        self.title('factorial (x)')
        self.geometry('250x100')
        self.resizable(0,0)
        self.number = Entry(self, width=32)
        self.solve = Button(self, text= '!', fg = 'blue', height=1, width=3, command = lambda event='<Button-1>' : MyApp.fctr(self))
        self.out = Label(self, text = '', fg = 'green', font = 16)
        self.number.bind('<Return>', lambda event= '<Return>' : MyApp.fctr(self))
        self.number.place(x=25,y=5)
        self.solve.place(x= 105, y = 30)
        self.out.place(x=25, y = 65)
        self.mainloop()
        
    def fctr(self):
        self.out.configure(text = '',fg='green')
        try:
            x = int(self.number.get())
            y = 1
            for elem in range(1, x+1):
                y*=elem
            self.out.configure(text = y)
        except:
            self.out.configure(text = 'ERROR',fg='red')
            
app = MyApp()
