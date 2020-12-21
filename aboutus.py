from tkinter import *



class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+550+120")
        self.title("About Us")
        self.resizable(False, False)

        self.top = Frame(self, height=550,width=550, bg="#ffa500")
        self.top.pack(fill=BOTH)

        self.text = Label(self.top,text='Hey this is about us page'
                          '\n this application is made for educational purpose'
                          '\n you can contact us on'
                          '\n Facebook = https://facebook.com/programingcage'
                          '\n instagram = ASM Technologies',
                          font = 'arial 14 bold',bg="#ffa500",fg="white")
        self.text.place(x=50,y=50)

