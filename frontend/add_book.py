from tkinter import *
import tkinter as tkr
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox
import model.book
import backend.db_connection


class AddBook:

    def __init__(self, root):
        self.root = root
        self.root.title("Add Book")
        self.root.geometry("335x560+500+100")
        self.root.iconbitmap("frontend\\Picture\\Icons\\Icon.ico")

        self.db = backend.db_connection.DBConnect()
        Title = Label(self.root, text="Add Book",
                      font=("comforta", 20, "bold"), compound=RIGHT, bg="#1A333A", fg="white")
        Title.pack(side=TOP, fill=X)

        def ireset():
            self.txtbooktitle.delete(0, END)
            self.txtbookauthor.delete(0, END)
            self.txtISBN.delete(0, END)
            self.txtGenre.delete(0, END)
            self.txtdate.delete(0, END)
            self.txtbook_price.delete(0, END)
            self.txtavailable.delete(0, END)

            self.txtbooktitle.insert(0, '')
            self.txtbookauthor.insert(0, '')
            self.txtISBN.insert(0, '')
            self.txtGenre.insert(0, '')
            self.txtdate.insert(0, '')
            self.txtbook_price.insert(0, '')
            self.txtavailable.insert(0, '')

            self.txtbooktitle.focus()

        self.bookdetail = Frame(root, bg="black", bd=5, width=335, height=520, padx=3, relief=GROOVE)
        self.bookdetail.place(x=0, y=38)

        # ************************BOOKS DETAIL***********************
        self.lblbooktitle = Label(self.bookdetail, font=('times', 10, 'bold'), text="Book Title      :", bg="black",
                                  fg="white")
        self.lblbooktitle.place(x=10, y=230)
        self.txtbooktitle = Entry(self.bookdetail)
        self.txtbooktitle.place(x=120, y=230, width=162)

        self.lblbookauthor = Label(self.bookdetail, font=('times', 10, 'bold'), text="Author            :", bg="black",
                                   fg="white")
        self.lblbookauthor.place(x=10, y=260)
        self.txtbookauthor = Entry(self.bookdetail)
        self.txtbookauthor.place(x=120, y=260, width=162)

        self.lblISBN = Label(self.bookdetail, font=('times', 10, 'bold'), text="ISBN   no.       :", bg="black",
                             fg="white")
        self.lblISBN.place(x=10, y=290)
        self.txtISBN = Entry(self.bookdetail)
        self.txtISBN.place(x=120, y=290, width=162)

        self.lblGenre = Label(self.bookdetail, font=('times', 10, 'bold'), text="Genre              :", bg="black",
                              fg="white")
        self.lblGenre.place(x=10, y=320)
        self.txtGenre = Entry(self.bookdetail)
        self.txtGenre.place(x=120, y=320, width=162)

        self.lbldate = Label(self.bookdetail, font=('times', 10, 'bold'), text="Released Date:", bg="black", fg="white")
        self.lbldate.place(x=10, y=350)
        self.txtdate = Entry(self.bookdetail)
        self.txtdate.place(x=120, y=350, width=162)

        self.lblbook_price = Label(self.bookdetail, font=('times', 10, 'bold'), text="Price (NPR)   :", bg="black",
                                   fg="white")
        self.lblbook_price.place(x=10, y=380)
        self.txtbook_price = Entry(self.bookdetail)
        self.txtbook_price.place(x=120, y=380, width=162)

        self.lblavailable = Label(self.bookdetail, font=('times', 10, 'bold'), text="Availability     :", bg="black",
                                  fg="white")
        self.lblavailable.place(x=10, y=410)
        self.txtavailable = Entry(self.bookdetail)
        self.txtavailable.place(x=120, y=410, width=162)

        # ************************************BUTTON******************************
        self.btn_reset = Button(self.bookdetail, text='Reset', font=('times', 10, 'bold'), bg="#db2020", fg="white",
                                width=7, bd=2, relief=GROOVE, command=ireset)
        self.btn_reset.place(x=200, y=460)

        self.btn_add = Button(self.bookdetail, text='Add Book', font=('times', 10, 'bold'), compound=LEFT, bg="#5cb85c",
                              fg="white", bd=2, relief=GROOVE, command=lambda: self.bookadd())
        self.btn_add.place(x=60, y=460)

    def bookadd(self):
        booktitle = self.txtbooktitle.get()
        author = self.txtbookauthor.get()
        isbn = self.txtISBN.get()
        genre = self.txtGenre.get()
        release_date = self.txtdate.get()
        price = self.txtbook_price.get()
        availability = self.txtavailable.get()

        if booktitle == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter Book Title!")
            self.txtbooktitle.focus()
            return
        elif author == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter Author Name!")
            self.txtbookauthor.focus()
            return
        elif isbn == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter ISBN Number!")
            self.txtISBN.focus()
            return
        elif genre == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter Book Genre!")
            self.txtGenre.focus()
            return
        elif release_date == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter Release Date!")
            self.txtdate.focus()
            return
        elif price == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter Book Price!")
            self.txtbook_price.focus()
            return
        elif availability == '':
            tkinter.messagebox.showerror("Bookstore Signup", "Please enter Book Availability!")
            self.txtavailable.focus()
            return
        else:
            b = model.book.Book(booktitle, author, isbn, genre, release_date, price, availability)

            query = "insert into book_info(book_title, author, isbn_no, genre, release_date, price, availability)" \
                    " values (%s, %s, %s, %s, %s, %s, %s) "
            values = (b.get_booktitle(), b.get_author(), b.get_isbn(), b.get_genre(), b.get_release_date(),
                      b.get_price(), b.get_availability())

            self.db.insert(query, values)
            tkinter.messagebox.showinfo('Bookstore', 'Book Added Successfully.')
            return
