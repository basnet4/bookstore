import pygame
import time
from pygame import mixer
import tkinter as tkr
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import frontend.bookstore_signup


class bookstorelogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("620x430+450+150")
        self.root.iconbitmap("frontend\\Picture\\Icons\\Icon.ico")
        self.root.title("Book Store Login ")
        self.root.configure(background='white')
        self.root.resizable(0, 0)

        self.image = Image.open("frontend\\Picture\\login_1.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        lbl = Label(self.root, image=self.photo)
        lbl.image = self.photo
        lbl.place(x=-30, y=0)

        self.password_icon = PhotoImage(file="frontend\\Picture\\Icons\\Password.png")
        self.Username_icon = PhotoImage(file="frontend\\Picture\\Icons\\Login1.png")
        self.exit_icon = PhotoImage(file="frontend\\Picture\\Icons\\Exit.png")

        Title = Label(self.root, text="   Bookstore Login   ",
                      font=("comforta", 20, "bold"), compound=RIGHT, bg="#301406", fg="white")
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
        def authenticate(username, password):
            if len(username) != 0 and len(password) != 0:
                if username == "Admin" and password == "Admin":
                    root.destroy()
                    mixer.music.fadeout(3000)
                    tkinter.messagebox.showinfo("login", "dashboard")
                    return
                else:
                    tkinter.messagebox.showerror("Book Store Login", "Invalid username or password!")
                    self.txtPassword.focus()
                    return
            elif len(username) == 0:
                tkinter.messagebox.showerror("Book Store Login", "Please enter username!")
                self.txtusername.focus()
                return
            else:
                tkinter.messagebox.showerror("Book Store Login", "Please enter password!")
                self.txtPassword.focus()
                return

        def sign_up():
            tk = Toplevel()
            root.withdraw()
            frontend.bookstore_signup.bookstoresignup(tk)

        def iexit():
            iexit = tkinter.messagebox.askyesno("Book Store Login", "Are you sure want to exit.")
            if iexit > 0:
                root.quit()
                return

        def f_password():
            tkinter.messagebox.showinfo("Book Store Login",
                                        "Change your Username and Password manually in code.")
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
                                command=lambda: authenticate(self.txtusername.get(), self.txtPassword.get()))
        self.root.bind("<Return>", lambda event: authenticate(self.txtusername.get(), self.txtPassword.get()))
        self.btn_login.place(x=445, y=350)

        self.btn_Signup = Button(root, text='Sign Up', font=('times', 10, 'bold'), bg="#2b83b2", fg="white", width=7,
                                 bd=2, relief=GROOVE, command=sign_up)
        self.btn_Signup.place(x=350, y=350)

        self.btn_Forgot = Button(login_frame, font=('times', 8), text="Forgotten your username or password?:", bd=0,
                                 bg="white", fg="blue", command=f_password)
        self.btn_Forgot.place(x=20, y=85)
