from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+230+120")
        self.title("Add New People")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#34baeb")
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file="icon/addpeople.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=130, y=33)

        # top frame heading
        self.heading = Label(self.top, text="Add People", font="arial 15 bold", bg="white", fg="#ebb434")
        self.heading.place(x=230, y=50)

        #name
        self.label_name = Label(self.bottom, text="Name",font="arial 15 bold",fg="white",bg="#ebb134")
        self.label_name.place(x=40,y=40)

        self.entry_name = Entry(self.bottom,width=30,bd=5)
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=150,y=40)

        #Surname
        self.label_surname = Label(self.bottom, text="Surname",font="arial 15 bold",fg="white",bg="#ebb134")
        self.label_surname.place(x=40,y=80)

        self.entry_surname = Entry(self.bottom,width=30,bd=5)
        self.entry_surname.insert(0,"Enter Surname")
        self.entry_surname.place(x=150,y=80)
        #email
        self.label_email = Label(self.bottom, text="E-mail",font="arial 15 bold",fg="white",bg="#ebb134")
        self.label_email.place(x=40,y=120)

        self.entry_email = Entry(self.bottom,width=30,bd=5)
        self.entry_email.insert(0,"Enter E-mail")
        self.entry_email.place(x=150,y=120)
        #phonenumber
        self.label_number = Label(self.bottom, text="Phone No",font="arial 15 bold",fg="white",bg="#ebb134")
        self.label_number.place(x=40,y=160)

        self.entry_number = Entry(self.bottom,width=30,bd=5)
        self.entry_number.insert(0,"Enter Phone Number")
        self.entry_number.place(x=150,y=160)
        #address
        self.label_address = Label(self.bottom, text="Address",font="arial 15 bold",fg="white",bg="#ebb134")
        self.label_address.place(x=40,y=200)

        self.entry_address = Text(self.bottom,width=23,height=8)
        self.entry_address.place(x=150,y=200)

        #button
        button=Button(self.bottom,text="Add Person",command=self.add_people)
        button.place(x=267,y=340)

    def add_people(self):
        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        number=self.entry_number.get()
        address=self.entry_address.get(1.0, 'end-1c')

        if name and surname and email and number and address != "":
            try:

                query = "insert into 'phonebook'(person_name,person_surname,person_email,person_number,person_address) values (?,?,?,?,?)"
                cur.execute(query, (name, surname, email, number, address))
                con.commit()
                messagebox.showinfo("Success","Contact Added")
            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Error","Fill all the fields",icon="warning")


