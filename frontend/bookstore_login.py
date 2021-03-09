import pygame
import time
from pygame import mixer
import tkinter as tkr
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import frontend.update_pass
import frontend.bookstore_signup
import frontend.bookstore_dashboard
import backend.db_connection


class bookstorelogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("620x430+450+150")
        self.root.iconbitmap("frontend\\Picture\\Icons\\Icon.ico")
        self.root.title("Bookstore Login ")
        self.root.configure(background='white')
        self.root.resizable(0, 0)

        self.db = backend.db_connection.DBConnect()
        self.image = Image.open("frontend\\Picture\\login_1.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        lbl = Label(self.root, image=self.photo)
        lbl.image = self.photo
        lbl.place(x=-30, y=0)

        self.password_icon = PhotoImage(file="frontend\\Picture\\Icons\\Password.png")
        self.Username_icon = PhotoImage(file="frontend\\Picture\\Icons\\Login1.png")
        self.exit_icon = PhotoImage(file="frontend\\Picture\\Icons\\Exit.png")

        Title = Label(self.root, text="   Bookstore Login   ",
                      font=("comforta", 20, "bold"), compound=RIGHT, bg="#1A333A", fg="white")
        Title.place(x=339, y=10)

        # ************************Clock***********************************

        label = Label(root, font=("Courier", 30, 'bold'), bg="black", fg="white")
        label.place(x=27, y=7)

        def digitalclock():
            text_input = time.strftime("%H:%M:%S %p")
            label.config(text=text_input)
            label.after(200, digitalclock)

        digitalclock()

        # ***********************MUSIC PLAYER*****************************
        self.stop_icon = PhotoImage(file="frontend\\Picture\\Icons\\Mute.png")
        self.play_icon = PhotoImage(file="frontend\\Picture\\Icons\\Play.png")
        mixer.init()
        mixer.music.load("frontend\\Music\\GOT.mp3")

        def Stop():
            pygame.mixer.music.fadeout(1000)

        def Play():
            pygame.mixer.music.play()

        pause_button = tkr.Button(root, image=self.stop_icon, command=Stop)
        pause_button.place(x=10, y=400)

        unpause_button = tkr.Button(root, image=self.play_icon, command=Play)
        unpause_button.place(x=40, y=400)

        # ***********************COMMAND**********************************

        def sign_up():
            self.root.withdraw()
            tk = Toplevel()
            frontend.bookstore_signup.bookstoresignup(tk)
            return

        def iexit():
            iexit = tkinter.messagebox.askyesno("Bookstore Login", "Are you sure want to exit.")
            if iexit > 0:
                pygame.mixer.music.fadeout(1000)
                root.quit()
                return

        def f_password():
            tk = Toplevel()
            frontend.update_pass.UP_pass(tk)
            return

        # ************************************FRAME**********************************
        login_frame = Frame(root, bg="white", bd=2, width=250, height=135, padx=2)
        login_frame.place(x=350, y=110)

        # ************************WIDGET****************************************

        self.lblusername = Label(login_frame, image=self.Username_icon, font=('times', 10, 'bold'), text="Username:",
                                 compound=LEFT, bg="white", fg="black")
        self.lblusername.place(x=10, y=15)
        self.txtusername = Entry(login_frame, bg="white")
        self.txtusername.focus()
        self.txtusername.place(x=110, y=18)

        self.lblPassword = Label(login_frame, image=self.password_icon, font=('times', 10, 'bold'), text="Password :",
                                 compound=LEFT, bg="white", fg="black")
        self.lblPassword.place(x=10, y=50)
        self.txtPassword = Entry(login_frame, show="*", bg="white")
        self.txtPassword.place(x=110, y=53)

        # #***************************Button****************************************

        self.btn_exit = Button(root, image=self.exit_icon, text='Exit', font=('times', 10, 'bold'), bg="#db2020",
                               fg="white", compound=LEFT, height=18, width=50, bd=2, relief=GROOVE, command=iexit)
        self.btn_exit.place(x=540, y=350)
        self.root.bind("<Escape>", lambda event: iexit())

        self.btn_login = Button(root, text='Log In', font=('times', 10, 'bold'), bg="#5cb85c", fg="white", width=7,
                                bd=2, relief=GROOVE,
                                command=lambda: self.authenticate())
        self.root.bind("<Return>", lambda event: self.authenticate())
        self.btn_login.place(x=445, y=350)

        self.btn_Signup = Button(root, text='Sign Up', font=('times', 10, 'bold'), bg="#2b83b2", fg="white", width=7,
                                 bd=2, relief=GROOVE, command=sign_up)
        self.btn_Signup.place(x=350, y=350)

        self.btn_Forgot = Button(login_frame, font=('times', 8), text="Forgotten your password?:", bd=0,
                                 bg="white", fg="blue", command=f_password)
        self.btn_Forgot.place(x=20, y=85)

    # *********************AUTHENTICATION FUNCTION**************************

    def authenticate(self):
        u_name = self.txtusername.get()
        p_word = self.txtPassword.get()

        if u_name == '':
            tkinter.messagebox.showerror("Bookstore Login Error", "Please enter username!")
            self.txtusername.focus()
            return
        elif p_word == '':
            tkinter.messagebox.showerror("Bookstore Login Error", "Please enter password!")
            self.txtPassword.focus()
            return
        else:
            query = "select * from sign_up where user_name=%s and pass_word=%s"
            values = (u_name, p_word)
            rows = self.db.select(query, values)
            data = []

            if len(rows) != 0:
                for row in rows:
                    data.append(row[0])
                    data.append(row[1])
                    data.append(row[2])
                    data.append(row[3])
                print(data)
                if u_name == data[2] and p_word == data[3]:
                    self.root.withdraw()
                    tk = Toplevel()
                    frontend.bookstore_dashboard.Bookstore(tk)

                else:
                    tkinter.messagebox.showerror("Bookstore Login Error", "!!! Invalid Username or password !!!")
            else:
                tkinter.messagebox.showinfo("Bookstore Login", "!!! User not registered !!!")
