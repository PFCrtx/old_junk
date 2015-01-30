import time
from tkinter import *

class Timer(Tk):
    
    def __init__ (self):
        Tk. __init__(self)
        self.geometry('160x40')
        self.resizable(0,0)
        self.start= round(time.time())
        self.m = Label(self,text='Seconds: ' + str(self.start),fg='green',font=30)
        self.m.place(x=35,y=8)
        time.sleep(1)
        self.tick()
        self.mainloop()

    def tick(self):
        self.m.configure(text='Seconds: '+str(round(time.time()-self.start)))
        self.after(1000, self.tick)
        
t = Timer()
