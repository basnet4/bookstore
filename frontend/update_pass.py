from tkinter import *
import tkinter.messagebox
import backend.db_connection


class UP_pass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x400+500+180")
        self.root.title("Bookstore info update")
        self.root.iconbitmap("frontend\\Picture\\Icons\\Icon.ico")
        self.root.configure(background="#292325")
        self.root.resizable(0, 0)
        self.db = backend.db_connection.DBConnect()

        Title = Label(self.root, text="  Update Password   ",
                      font=("comforta", 20, "bold"), compound=LEFT, bg="#1A333A", fg="#C0C0C0")
        Title.place(x=10, y=10)

        # ***************************WIDGET***************************************
        self.lbl_username = Label(root, font=('times', 10, 'bold'), text="Username:",
                                  compound=LEFT, bg="#292325", fg="#C0C0C0")
        self.lbl_username.place(x=50, y=80)
        self.txt_username = Entry(root, bg="#292325", fg="#C0C0C0")
        self.txt_username.focus()
        self.txt_username.place(x=51, y=100)

        self.lbl_newpass = Label(root, font=('times', 10, 'bold'), text="New Password :",
                                 compound=LEFT, bg="#292325", fg="#C0C0C0")
        self.lbl_newpass.place(x=50, y=130)
        self.txt_newpass = Entry(root, show="*", bg="#292325", fg="#C0C0C0")
        self.txt_newpass.place(x=51, y=150)

        self.lbl_confpass = Label(root, font=('times', 10, 'bold'), text="Confirm Password :",
                                  compound=LEFT, bg="#292325", fg="#C0C0C0")
        self.lbl_confpass.place(x=50, y=180)
        self.txt_confpass = Entry(root, show="*", bg="#292325", fg="#C0C0C0")
        self.txt_confpass.place(x=51, y=200)

        # *************************BUTTON********************
        self.btn_udate = Button(root, text='Update', font=('times', 10, 'bold'), bg="#2b83b2", fg="white", width=7,
                                bd=2, relief=GROOVE, command=lambda: self.up_date())
        self.btn_udate.place(x=120, y=280)
        self.root.bind("<Return>", lambda event: self.up_date())

    def up_date(self):
        username = self.txt_username.get()
        newpassword = self.txt_newpass.get()
        confpassword = self.txt_confpass.get()

        if username == '':
            tkinter.messagebox.showerror("Bookstore Error", "Please enter username!")
            self.txt_username.focus()
            return
        elif newpassword == '':
            tkinter.messagebox.showerror("Bookstore Error", "Please enter new password!")
            self.txt_newpass.focus()
            return
        elif confpassword == '':
            tkinter.messagebox.showerror("Bookstore Error", "Please confirm password!")
            self.txt_confpass.focus()
            return
        elif newpassword != confpassword:
            tkinter.messagebox.showerror("Bookstore Error", "!!! New password did not match with confirm password !!!")
            return
        else:
            query = "update sign_up set pass_word=%s where user_name=%s"
            values = (newpassword, username)

            self.db.update(query, values)
            tkinter.messagebox.showinfo("Bookstore info update", "Your password has been changed.")
            self.root.destroy()
            return
