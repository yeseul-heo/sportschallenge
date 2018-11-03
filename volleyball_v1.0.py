import csv
import os
from Tkinter import *

class Application(Frame):
    #Initial Settings
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.init_Buttons()
        root.title("GT Volleyball Analytics")

    #Place Initial Buttons
    def init_Buttons(self):
        #Three buttons for year, game, and player
        self.toptext = Label(text="Select Category:").place(relx=0.5, rely=0.2, anchor=CENTER)
        self.yearbutton = Button(text="Year").place(relx=0.5, rely=0.4, anchor=CENTER)
        self.gamebutton = Button(text="Game").place(relx=0.5, rely=0.5, anchor=CENTER)
        self.playerbutton = Button(text="Player").place(relx=0.5, rely=0.6, anchor=CENTER)

    

#Final settings to keep window open
root = Tk()
root.geometry("1000x400")
app = Application(master=root)
app.mainloop()
root.destroy()

#edit

