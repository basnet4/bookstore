from tkinter import *
import pygame
from pygame import mixer
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tkr
import tkinter.messagebox
import frontend.bookstore_login


class bookstoresignup:
    def __init__(self, root):
        self.root = root
        self.root.geometry("620x430+450+150")
        self.root.iconbitmap("frontend\\Picture\Icons\Icon.ico")
        self.root.title("Bookstore Signup ")
        self.root.configure(background='white')
        self.root.resizable(0, 0)

        self.image = Image.open("frontend\\Picture\\signup_1.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        lbl = Label(self.root, image=self.photo)
        lbl.place(x=-30, y=0)

        Title = Label(self.root, text="  Bookstore Signup  ",
                      font=("comforta", 20, "bold"), compound=RIGHT, bg="#18435C", fg="white")
        Title.place(x=338, y=10)

        # *******************************FRAME*****************************
        info_frame = Frame(root, bg="white", height=350, width=250)
        info_frame.place(x=350, y=50)

        # ***********************MUSIC PLAYER*****************************
        self.Stop_icon = PhotoImage(file="frontend\\Picture\Icons\Mute.png")
        self.Play_icon = PhotoImage(file="frontend\\Picture\Icons\Play.png")

        mixer.init()
        mixer.music.load("frontend\\Music\LOR.mp3")

        def Stop():
            pygame.mixer.music.fadeout(1000)

        def Play():
            pygame.mixer.music.play()

        play_button = tkr.Button(root, image=self.Stop_icon, command=Stop)
        play_button.place(x=10, y=400)

        pause_button = tkr.Button(root, image=self.Play_icon, command=Play)
        pause_button.place(x=40, y=400)

        self.btnsignup = Button(root, text='Sign Up', font=('times', 10, 'bold'), bg="#5cb85c", fg="white", width=7,
                                bd=2, relief=GROOVE, command=self.signup)
        self.root.bind("<Return>", lambda event: self.signup())
        self.btnsignup.place(x=445, y=390)

        # ************************WIDGET****************************************

        self.lblfirstname = Label(info_frame, font=('times', 10, 'bold'), text="First name:", bg="white", fg="black")
        self.lblfirstname.place(x=15, y=10)
        self.txtfirstname = Entry(info_frame, bg="white")
        self.txtfirstname.place(x=100, y=10)
        self.txtfirstname.focus()

        self.lblsurname = Label(info_frame, font=('times', 10, 'bold'), text="Surname   :", bg="white", fg="black")
        self.lblsurname.place(x=15, y=50)
        self.txtsurname = Entry(info_frame, bg="white")
        self.txtsurname.place(x=100, y=50)

        self.lblusername = Label(info_frame, font=('times', 10, 'bold'), text="Username :", bg="white", fg="black")
        self.lblusername.place(x=15, y=90)
        self.txtusername = Entry(info_frame, bg="white")
        self.txtusername.place(x=100, y=90)

        self.lblPassword = Label(info_frame, font=('times', 10, 'bold'), text="Password  :", bg="white", fg="black")
        self.lblPassword.place(x=15, y=130)
        self.txtPassword = Entry(info_frame, show="*", bg="white")
        self.txtPassword.place(x=100, y=130)

        self.lblmobno = Label(info_frame, font=('times', 10, 'bold'), text="Mobile no. :", bg="white", fg="black")
        self.lblmobno.place(x=15, y=170)
        self.txtmobno = Entry(info_frame, bg="white")
        self.txtmobno.place(x=100, y=170)

        self.lblmembertype = Label(info_frame, font=('times', 10, 'bold'), text="Date of Birth:", bg="white",
                                   fg="black")
        self.lblmembertype.place(x=15, y=210)

        self.cbo_day = ttk.Combobox(info_frame, font=('times', 10, 'bold'), state='readonly', width=3)
        self.cbo_day['value'] = (
            'Day', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
        self.cbo_day.current(0)
        self.cbo_day.place(x=15, y=240)

        self.cbo_mon = ttk.Combobox(info_frame, font=('times', 10, 'bold'), state='readonly', width=5)
        self.cbo_mon['value'] = (
            'Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
        self.cbo_mon.current(0)
        self.cbo_mon.place(x=70, y=240)

        self.cbo_year = ttk.Combobox(info_frame, font=('times', 10, 'bold'), state='readonly', width=7)
        self.cbo_year['value'] = ('Year', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
                                  '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                                  '2009', '2010',
                                  '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                                  '2021')
        self.cbo_year.current(0)
        self.cbo_year.place(x=140, y=240)

        self.lblgender = Label(info_frame, font=('times', 10, 'bold'), text="Gender :", bg="white", fg="black")
        self.lblgender.place(x=15, y=280)

        self.cbo_gen = ttk.Combobox(info_frame, font=('times', 10, 'bold'), state='readonly', width=5)
        self.cbo_gen['value'] = ('', 'Male', 'Female', 'Other')
        self.cbo_gen.current(0)
        self.cbo_gen.place(x=15, y=310)

        # ***************************Button****************************************
        def s_exit():
            iexit = tkinter.messagebox.askyesno("Book Store Login", "Are you sure want to exit.")
            if iexit > 0:
                pygame.mixer.music.fadeout(1000)
                root.destroy()
                return

        self.root.bind("<Escape>", lambda event: s_exit())

    def signup(self):
        firstname = self.txtfirstname.get()
        surname = self.txtsurname.get()
        username = self.txtusername.get()
        password = self.txtPassword.get()
        mobile = self.txtmobno.get()
        dob = self.cbo_day.get() + '-' + self.cbo_mon.get() + '-' + self.cbo_year.get()
        gender = self.cbo_gen.get()

        if firstname == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter your firstname!")
            self.txtfirstname.focus()
            return
        elif surname == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter your surname!")
            self.txtsurname.focus()
            return
        elif username == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter your username!")
            self.txtusername.focus()
            return
        elif password == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter new password!")
            self.txtPassword.focus()
            return
        elif mobile == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter your mobile number!")
            self.txtmobno.focus()
            return
        elif dob == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter your date of birth!")
            self.cbo_day.focus()
            return
        elif gender == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter your gender!")
            self.cbo_gen.focus()
            return
        else:
            tkinter.messagebox.showinfo('Bookstore Sign up', 'Successfully  Signed up.')
            self.root.destroy()
            tk = Toplevel()
            frontend.bookstore_login.bookstorelogin(tk)
            return
