from tkinter import *
import tkinter.messagebox
import backend.db_connection


class Del_User:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x400+500+180")
        self.root.title("Bookstore delete user")
        self.root.iconbitmap("frontend\\Picture\\Icons\\Icon.ico")
        self.root.configure(background="#292325")
        self.root.resizable(0, 0)
        self.db = backend.db_connection.DBConnect()

        Title = Label(self.root, text="        Delete User       ",
                      font=("comforta", 20, "bold"), compound=LEFT, bg="#1A333A", fg="#C0C0C0")
        Title.place(x=10, y=10)

        # ***************************WIDGET***************************************
        self.lbl_username = Label(root, font=('times', 10, 'bold'), text="Username:",
                                  compound=LEFT, bg="#292325", fg="#C0C0C0")
        self.lbl_username.place(x=50, y=80)
        self.txt_username = Entry(root, bg="#292325", fg="#C0C0C0")
        self.txt_username.focus()
        self.txt_username.place(x=51, y=100)

        self.lbl_pass = Label(root, font=('times', 10, 'bold'), text="Password :",
                              compound=LEFT, bg="#292325", fg="#C0C0C0")
        self.lbl_pass.place(x=50, y=130)
        self.txt_pass = Entry(root, show="*", bg="#292325", fg="#C0C0C0")
        self.txt_pass.place(x=51, y=150)

        self.lbl_confpass = Label(root, font=('times', 10, 'bold'), text="Confirm Password :",
                                  compound=LEFT, bg="#292325", fg="#C0C0C0")
        self.lbl_confpass.place(x=50, y=180)
        self.txt_confpass = Entry(root, show="*", bg="#292325", fg="#C0C0C0")
        self.txt_confpass.place(x=51, y=200)

        # *************************BUTTON********************
        self.btn_udate = Button(root, text='Delete', font=('times', 10, 'bold'), bg="#db2020", fg="white", width=7,
                                bd=2, relief=GROOVE, command=lambda: self.del_user())
        self.btn_udate.place(x=120, y=280)
        self.root.bind("<Return>", lambda event: self.del_user())

    def del_user(self):
        username = self.txt_username.get()
        password = self.txt_pass.get()
        confpassword = self.txt_confpass.get()

        if username == '':
            tkinter.messagebox.showerror("Bookstore Error", "Please enter username!")
            self.txt_username.focus()
            return
        elif password == '':
            tkinter.messagebox.showerror("Bookstore Error", "Please enter password!")
            self.txt_pass.focus()
            return
        elif confpassword == '':
            tkinter.messagebox.showerror("Bookstore Error", "Please confirm password!")
            self.txt_confpass.focus()
            return
        elif password != confpassword:
            tkinter.messagebox.showerror("Bookstore Error", "!!! New password did not match with confirm password !!!")
            return
        else:
            query = "delete from sign_up where user_name=%s"
            values = (username,)

            self.db.delete(query, values)
            tkinter.messagebox.askyesno("Bookstore delete user", "Are you sure you want to delete?")
            self.root.destroy()
            return
