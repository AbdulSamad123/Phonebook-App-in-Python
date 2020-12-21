from tkinter import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About

date = datetime.datetime.now().date()
date = str(date)


class Application(object):

    def __init__(self, master):
        self.master = master

        # Frames

        self.top = Frame(master, height=150, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg="#34baeb")
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file="icon/logo.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=130, y=35)

        # top frame heading
        self.heading = Label(self.top, text="My Phonebook App", font="arial 15 bold", bg="white", fg="#ebb434")
        self.heading.place(x=230, y=50)

        self.date_label = Label(self.top, text="Today's Date: " + date, font="arial 12 bold", bg="white", fg="#ebb434")
        self.date_label.place(x=450, y=110)

        # button-1 (view people)
        self.viewButton = Button(self.bottom, text="   My People   ", font="arial 12 bold", fg="#42bcf5", bg="white",command=self.my_people)
        self.viewButton.place(x=250, y=70)
        # button-2 (add people)
        self.addButton = Button(self.bottom, text="  Add People  ", font="arial 12 bold", fg="#42bcf5", bg="white",command=self.addpeoplefunction)
        self.addButton.place(x=250, y=130)
        # button-3(about us)
        self.aboutButton = Button(self.bottom, text="    About Us    ", font="arial 12 bold", fg="#42bcf5", bg="white",command=self.about_us)
        self.aboutButton.place(x=250, y=190)

    def my_people(self):
        people = MyPeople()
    def about_us(self):
        aboutpage = About()
    def addpeoplefunction(self):
        addpeoplewindow = AddPeople()


def main():
    root = Tk()
    app = Application(root)
    root.title("Phonebook Application")
    root.geometry("650x550+350+100")
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
