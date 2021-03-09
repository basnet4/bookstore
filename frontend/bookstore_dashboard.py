from tkinter import *
from tkinter import ttk
from tkinter import Menu
from PIL import Image, ImageTk
import tkinter.messagebox
import frontend.delete_user


class Bookstore:

    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Book Store Management System")
        self.root.geometry("1366x778+0+0")
        self.root.iconbitmap("frontend\\Picture\\Icons\\Icon.ico")

        self.image = Image.open("frontend\\Picture\PIC1.jpg")
        self.photo = ImageTk.PhotoImage(self.image)

        lbl = Label(self.root, image=self.photo)
        lbl.pack(pady=0, padx=0)

        self.Add_icon = PhotoImage(file="frontend\\Picture\Icons\Add.png")

        # *********************COMMAND************************
        # ****************************************************
        def done(firstname, surname, address, mobile_num, email, date, Booktitle, price, quantity, discountount):
            if len(firstname) != 0 and len(surname) != 0 and len(address) != 0 and len(mobile_num) != 0 and len(
                    email) != 0 and len(date) != 0 and len(Booktitle) != 0 and len(price) != 0 and \
                    len(quantity) != 0 and len(discountount) != 0:
                tkinter.messagebox.showinfo("Book Store Management System", "Data Stored.")
                return
            elif (len(firstname) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter firstname!")
                self.txtfirstname.focus()
                return
            elif (len(surname) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter surname!")
                self.txtsurname.focus()
                return
            elif (len(address) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter address!")
                self.txtaddress.focus()
                return
            elif (len(mobile_num) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter mobile number!")
                self.txtmobile_no.focus()
                return
            elif (len(email) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter email!")
                self.txtemail.focus()
                return
            elif (len(date) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter today's date!")
                self.txt_date.focus()
                return
            elif (len(Booktitle) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter book name!")
                self.txt_Booktitle.focus()
                return
            elif (len(price) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter book price!")
                self.txtPrice.focus()
                return
            elif (len(quantity) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter quantity!")
                self.txtqty.focus()
                return
            else:
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter discountount!")
                self.txtdiscount.focus()
                return

        def bookadd():
            tkinter.messagebox.showinfo("Book Store Management System ", "Book Added Successfully.")
            return

        # *****************FOR BOOK DETAIL***********************
        booktitle = StringVar()
        author = StringVar()
        ISBN = StringVar()
        genre = StringVar()
        releasedate = StringVar()
        bookprice = StringVar()
        availability = StringVar()
        search = StringVar()

        def ireset():
            booktitle.set("")
            author.set("")
            ISBN.set("")
            genre.set("")
            releasedate.set("")
            bookprice.set("")
            availability.set("")
            search.set("")
            self.P_lbl.destroy()

        # *********************FOR CUSTOMER DETAIL********************
        title = StringVar()
        firstname = StringVar()
        surname = StringVar()
        address = StringVar()
        mobile = StringVar()
        email = StringVar()
        date = StringVar()
        Booktitle = StringVar()
        price = StringVar()
        quantity = StringVar()
        discountount = StringVar()

        def iclear():
            title.set("")
            firstname.set("")
            surname.set("")
            address.set("")
            mobile.set("")
            email.set("")
            date.set("")
            Booktitle.set("")
            price.set("")
            quantity.set("")
            discountount.set("")

        def i_exit():
            i_exit = tkinter.messagebox.askyesno("Book Store Management System", "Are you sure want to exit.")
            if i_exit > 0:
                root.destroy()
                return

        def d_user():
            tk = Toplevel()
            frontend.delete_user.Del_User(tk)
            return

        # *******************************MENU************************************

        self.menu = Menu(self.root)
        self.file_new_item = Menu(self.menu)
        # self.file_new_item.add_separator()
        self.file_new_item.add_command(label='Edit System Profile')
        self.file_new_item.add_command(label='Delete User', command=lambda: d_user())
        self.file_new_item.add_command(label="Exit", command=i_exit)
        self.menu.add_cascade(label='File', menu=self.file_new_item)

        self.vendor_new_item = Menu(self.menu)
        self.vendor_new_item.add_command(label='Add Vendor')
        self.vendor_new_item.add_command(label='View All Vendors')
        self.menu.add_cascade(label='Vendor', menu=self.vendor_new_item)

        self.book_new_item = Menu(self.menu)
        self.book_new_item.add_command(label='Books Available')
        self.book_new_item.add_command(label='Add Book')
        self.menu.add_cascade(label='Books', menu=self.book_new_item)

        self.customer_new_item = Menu(self.menu)
        self.customer_new_item.add_command(label='Add Customer')
        self.customer_new_item.add_command(label='View All Customer')
        self.menu.add_cascade(label='Customer', menu=self.customer_new_item)

        self.order_new_item = Menu(self.menu)
        self.order_new_item.add_command(label='Add Order')
        self.order_new_item.add_command(label='View All Orders')
        self.menu.add_cascade(label='Order', menu=self.order_new_item)

        self.help_new_item = Menu(self.menu)
        self.help_new_item.add_command(label='Help')
        self.help_new_item.add_command(label='Check for Updates..')
        self.help_new_item.add_separator()
        self.help_new_item.add_command(label='About')
        self.menu.add_cascade(label='Help', menu=self.help_new_item)

        self.root.config(menu=self.menu)

        # ***********************TITLE*****************************

        Title = Label(self.root, text="         Customer  Detail          ", font=("comforta", 20, "bold"), bg="black",
                      fg="#c97e21", relief=GROOVE)
        Title.place(x=50, y=35)

        Title = Label(self.root, text="  Book  Genre  ", font=("comforta", 20, "bold"), bg="black", fg="#c97e21",
                      relief=GROOVE)
        Title.place(x=495, y=35)

        Title = Label(self.root, text="    Book  List    ", font=("comforta", 20, "bold"), bg="black", fg="#c97e21",
                      relief=GROOVE)
        Title.place(x=715, y=35)

        Title = Label(self.root, text="         Books   Detail          ", font=("comforta", 20, "bold"), bg="black",
                      fg="#c97e21", relief=GROOVE)
        Title.place(x=970, y=35)

        # ************************BOOK GENRE LIST FUNCTIONS***************************
        def Adventure():
            try:
                x = ("frontend\\Book Genre TXT\Adventure.txt")
                T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
                T.place(x=2, y=2)
                T.insert(END, open(x).read())
            except FileNotFoundError as fnf_error:
                tkinter.messagebox.showerror("Book Store Management System", fnf_error)

        def Biography():
            try:
                x = ("frontend\\Book Genre TXT\Biography.txt")
                T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
                T.place(x=2, y=2)
                T.insert(END, open(x).read())
            except Exception as error:
                tkinter.messagebox.showinfo("Book Store Management System", error)

        def Fantasy():
            x = ("frontend\\Book Genre TXT\Fantasy.txt")
            T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
            T.place(x=2, y=2)
            T.insert(END, open(x).read())

        def Fiction():
            x = ("frontend\\Book Genre TXT\Fiction.txt")
            T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
            T.place(x=2, y=2)
            T.insert(END, open(x).read())

        def History():
            x = ("frontend\\Book Genre TXT\History.txt")
            T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
            T.place(x=2, y=2)
            T.insert(END, open(x).read())

        def Horror():
            x = ("frontend\\Book Genre TXT\Horror.txt")
            T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
            T.place(x=2, y=2)
            T.insert(END, open(x).read())

        def N_fiction():
            x = ("frontend\\Book Genre TXT\\Non_Fiction.txt")
            T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
            T.place(x=2, y=2)
            T.insert(END, open(x).read())

        def Novel():
            x = ("frontend\\Book Genre TXT\\Novel.txt")
            T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
            T.place(x=2, y=2)
            T.insert(END, open(x).read())

        def Thriller():
            x = ("frontend\\Book Genre TXT\\Thiller.txt")
            T = Text(bookgenre, state='normal', height=6, width=50, bg='black', fg='white', bd=0)
            T.place(x=2, y=2)
            T.insert(END, open(x).read())

        # ***********************BOOK GENRE BOTTON************************
        self.btngenre_adventure = Button(root, text='AVENTURE', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                         width=20, bd=3, relief=GROOVE, command=Adventure)
        self.btngenre_adventure.place(x=500, y=100)

        self.btngenre_biography = Button(root, text='BIOGRAPHY', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                         width=20, bd=3, relief=GROOVE, command=Biography)
        self.btngenre_biography.place(x=500, y=150)

        self.btngenre_fantasy = Button(root, text='FANTASY', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                       width=20, bd=3, relief=GROOVE, command=Fantasy)
        self.btngenre_fantasy.place(x=500, y=200)

        self.btngenre_fiction = Button(root, text='FICTION', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                       width=20, bd=3, relief=GROOVE, command=Fiction)
        self.btngenre_fiction.place(x=500, y=250)

        self.btngenre_history = Button(root, text='HISTORY', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                       width=20, bd=3, relief=GROOVE, command=History)
        self.btngenre_history.place(x=500, y=300)

        self.btngenre_horror = Button(root, text=' HORROR ', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                      width=20, bd=3, relief=GROOVE, command=Horror)
        self.btngenre_horror.place(x=500, y=350)

        self.btngenre_non_fiction = Button(root, text='NON-FICTION', font=('Comfortaa', 9, 'bold'), bg="black",
                                           fg="white", width=20, bd=3, relief=GROOVE, command=N_fiction)
        self.btngenre_non_fiction.place(x=500, y=400)

        self.btngenre_novel = Button(root, text='NOVEL', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                     width=20, bd=3, relief=GROOVE, command=Novel)
        self.btngenre_novel.place(x=500, y=450)

        self.btngenre_thriller = Button(root, text='THRILLER', font=('Comfortaa', 9, 'bold'), bg="black", fg="white",
                                        width=20, bd=3, relief=GROOVE, command=Thriller)
        self.btngenre_thriller.place(x=500, y=500)

        # ************************FRAME******************************
        bookframe = Frame(root, bg="black", bd=5, width=160, height=435, padx=3, relief=GROOVE)
        bookframe.place(x=710, y=100)

        bookdetail = Frame(root, bg="black", bd=5, width=335, height=520, padx=3, relief=GROOVE)
        bookdetail.place(x=975, y=130)

        bookgenre = Frame(root, bg="black", bd=2, width=418, height=110, padx=3, relief=GROOVE)
        bookgenre.place(x=500, y=540)

        c_detail = Frame(root, bg="black", bd=5, width=380, height=550, padx=3, relief=GROOVE)
        c_detail.place(x=50, y=100)

        # ************************WIDGET**CUSTOMER DETAIL****************************

        self.lblTitle = Label(c_detail, font=('times', 10, 'bold'), text="Title             :", bg="black", fg="white")
        self.lblTitle.place(x=20, y=20)

        self.cboTitle = ttk.Combobox(c_detail, state='readonly', font=('times', 10, 'bold'), textvariable=title)
        self.cboTitle['value'] = ('', 'Mr.', 'Miss.', 'Mrs.', 'Dr.', 'Capt.', 'Ms.')
        self.cboTitle.place(x=120, y=20)

        self.lblfirstname = Label(c_detail, font=('times', 10, 'bold'), text="Firstname   :", bg="black", fg="white")
        self.lblfirstname.place(x=20, y=60)
        self.txtfirstname = Entry(c_detail, textvariable=firstname)
        self.txtfirstname.place(x=120, y=60, width=162)

        self.lblsurname = Label(c_detail, font=('times', 10, 'bold'), text="Surname     :", bg="black", fg="white")
        self.lblsurname.place(x=20, y=100)
        self.txtsurname = Entry(c_detail, textvariable=surname)
        self.txtsurname.place(x=120, y=100, width=162)

        self.lbladdress = Label(c_detail, font=('times', 10, 'bold'), text="Address       :", bg="black", fg="white")
        self.lbladdress.place(x=20, y=140)
        self.txtaddress = Entry(c_detail, textvariable=address)
        self.txtaddress.place(x=120, y=140, width=162)

        self.lblmobile_no = Label(c_detail, font=('times', 10, 'bold'), text="Mobile no.    :", bg="black", fg="white")
        self.lblmobile_no.place(x=20, y=180)
        self.txtmobile_no = Entry(c_detail, textvariable=mobile)
        self.txtmobile_no.place(x=120, y=180, width=162)

        self.lblemail = Label(c_detail, font=('times', 10, 'bold'), text="Email            :", bg="black", fg="white")
        self.lblemail.place(x=20, y=220)
        self.txtemail = Entry(c_detail, textvariable=email)
        self.txtemail.place(x=120, y=220, width=162)

        self.lbl_date = Label(c_detail, font=('times', 10, 'bold'), text="Date              :", bg="black", fg="white")
        self.lbl_date.place(x=20, y=260)
        self.txt_date = Entry(c_detail, textvariable=date)
        self.txt_date.place(x=120, y=260, width=162)

        self.lbl_Booktitle = Label(c_detail, font=('times', 10, 'bold'), text="Book Title   :", bg="black", fg="white")
        self.lbl_Booktitle.place(x=20, y=300)
        self.txt_Booktitle = Entry(c_detail, textvariable=Booktitle)
        self.txt_Booktitle.place(x=120, y=300, width=162)

        self.lblPrice = Label(c_detail, font=('times', 10, 'bold'), text="Price (NPR):", bg="black", fg="white")
        self.lblPrice.place(x=20, y=340)
        self.txtPrice = Entry(c_detail, textvariable=price)
        self.txtPrice.place(x=120, y=340, width=162)

        self.lblqty = Label(c_detail, font=('times', 10, 'bold'), text="Quantity      :", bg="black", fg="white")
        self.lblqty.place(x=20, y=380)
        self.txtqty = Entry(c_detail, textvariable=quantity)
        self.txtqty.place(x=120, y=380, width=162)

        self.lbldiscount = Label(c_detail, font=('times', 10, 'bold'), text="discount       :", bg="black",
                                 fg="white")
        self.lbldiscount.place(x=20, y=420)
        self.txtdiscount = Entry(c_detail, textvariable=discountount)
        self.txtdiscount.place(x=120, y=420, width=162)

        # ************************BOOKS DETAIL***********************
        self.lblbooktitle = Label(bookdetail, font=('times', 10, 'bold'), text="Book Title      :", bg="black",
                                  fg="white")
        self.lblbooktitle.place(x=10, y=230)
        self.txtbooktitle = Entry(bookdetail, textvariable=booktitle)
        self.txtbooktitle.place(x=120, y=230, width=162)

        self.lblbookauthor = Label(bookdetail, font=('times', 10, 'bold'), text="Author            :", bg="black",
                                   fg="white")
        self.lblbookauthor.place(x=10, y=260)
        self.txtbookauthor = Entry(bookdetail, textvariable=author)
        self.txtbookauthor.place(x=120, y=260, width=162)

        self.lblISBN = Label(bookdetail, font=('times', 10, 'bold'), text="ISBN   no.       :", bg="black", fg="white")
        self.lblISBN.place(x=10, y=290)
        self.txtISBN = Entry(bookdetail, textvariable=ISBN)
        self.txtISBN.place(x=120, y=290, width=162)

        self.lblGenre = Label(bookdetail, font=('times', 10, 'bold'), text="Genre              :", bg="black",
                              fg="white")
        self.lblGenre.place(x=10, y=320)
        self.txtGenre = Entry(bookdetail, textvariable=genre)
        self.txtGenre.place(x=120, y=320, width=162)

        self.lbldate = Label(bookdetail, font=('times', 10, 'bold'), text="Released Date:", bg="black", fg="white")
        self.lbldate.place(x=10, y=350)
        self.txtdate = Entry(bookdetail, textvariable=releasedate)
        self.txtdate.place(x=120, y=350, width=162)

        self.lblbook_price = Label(bookdetail, font=('times', 10, 'bold'), text="Price (NPR)   :", bg="black",
                                   fg="white")
        self.lblbook_price.place(x=10, y=380)
        self.txtbook_price = Entry(bookdetail, textvariable=bookprice)
        self.txtbook_price.place(x=120, y=380, width=162)

        self.lblavailable = Label(bookdetail, font=('times', 10, 'bold'), text="Availability     :", bg="black",
                                  fg="white")
        self.lblavailable.place(x=10, y=410)
        self.txtavailable = Entry(bookdetail, textvariable=availability)
        self.txtavailable.place(x=120, y=410, width=162)

        # ************************SEARCH****************************
        def Search_Btn(lst, search):
            if search != '':
                isFound = False
                for i in range(len(lst)):
                    if lst[i] == search:
                        isFound = True
                        break
                if (isFound):
                    if (search == "A CLASH OF KINGS"):
                        booktitle.set("A CLASH OF KING")
                        author.set("GEORGE R. R. MARTIN")
                        ISBN.set("0-553-10803-4 (US Hardback)")
                        genre.set("FANTASY")
                        releasedate.set("November 16, 1998")
                        bookprice.set("1000.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\A Clash of king.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "A DREAM OF SPRING"):
                        booktitle.set("A DREAM OF SPRING")
                        author.set("GEORGE R. R. MARTIN")
                        ISBN.set("0-553-102343-4")
                        genre.set("FANTASY")
                        releasedate.set("! NOT AVAILABILE")
                        bookprice.set("980.00")
                        availability.set("!NOT AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\A dream of spring.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "ARRESTTING GOD IN KTM"):
                        booktitle.set("ARRESTTING GOD IN KATHMANDU")
                        author.set("SAMRAT UPADHYAY")
                        ISBN.set("9780618043712")
                        genre.set("FICTION")
                        releasedate.set("2001")
                        bookprice.set("350.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Arresting god in ktm.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "CHINA HARAYEKO MANCHE"):
                        booktitle.set("CHINA HARAYEKO MANCHE")
                        author.set("HARI BANSHA ACHARYA")
                        ISBN.set("9937866642")
                        genre.set("BIOGRAPHY")
                        releasedate.set("APRIL 2013")
                        bookprice.set("285.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\China harayeko manche.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "FIVE POINT SOMEONE"):
                        booktitle.set("FIVE POINT SOMEONE")
                        author.set("CHETAN BHAGAT")
                        ISBN.set("81-291-0459-8")
                        genre.set("FICTION")
                        releasedate.set("4 AUGUST 2004")
                        bookprice.set("350.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Five Point Someone.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "GAME OF THRONES"):
                        booktitle.set("GAME OF THRONES")
                        author.set("GEORGE R. R. MARTIN")
                        ISBN.set("0-553-10354-7 (US hardback)")
                        genre.set("FANTASY")
                        releasedate.set("AUGUST 1, 1996")
                        bookprice.set("1010.00")
                        availability.set("!NOT AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Game of throness.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "THE GIRL IN ROOM 105"):
                        booktitle.set("THE GIRL IN ROOM 105")
                        author.set("CHETAN BHAGAT")
                        ISBN.set("978-1542040464")
                        genre.set("MYSTERY, THRILLER")
                        releasedate.set("OCTOBER 9, 2018")
                        bookprice.set("385.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Girl in room.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "HALF GIRLFRIEND"):
                        booktitle.set("HALF GIRLFRIEND")
                        author.set("CHETAN BHAGAT")
                        ISBN.set("978-81-291-3572-8")
                        genre.set("FICTION, ROMANCE")
                        releasedate.set("1 OCTOBER, 2014")
                        bookprice.set("375.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Half girlfiend.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "INDIA AFTER GANDHI"):
                        booktitle.set("INDIA AFTER GANDHI")
                        author.set("RAMCHANDRA GUHA")
                        ISBN.set("978-0-330-50554-3")
                        genre.set("NON-FICTION")
                        releasedate.set("24 JULY, 2007")
                        bookprice.set("1200.00")
                        availability.set("!NOT AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\India After gandi.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "INTO THE WILD"):
                        booktitle.set("INTO THE WILD")
                        author.set("JON KRAKAUER")
                        ISBN.set("0-679-42850-X")
                        genre.set("BIOGRAPHY")
                        releasedate.set("1996")
                        bookprice.set("800.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Into the wild.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "JIWAN KADA KI FUL"):
                        booktitle.set("JIWAN KADA KI FUL")
                        author.set("JHAMAK KUMAR GHIMIRE")
                        ISBN.set("978-9-93-722347-8")
                        genre.set("BIOGRAPHY")
                        releasedate.set("2010")
                        bookprice.set("250.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Jiwan Kanda Ki Phool.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "KARNALI BLUES"):
                        booktitle.set("KARNALI BLUES")
                        author.set("BUDDHI SAGAR")
                        ISBN.set("9789937827935")
                        genre.set("NOVEL, CONTEMPORARY FICTION")
                        releasedate.set("2010")
                        bookprice.set("350.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Karnali blues.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "LORD OF THE RING"):
                        booktitle.set("LORD OF THE RINGS")
                        author.set("J. R. R. TOLKIEN")
                        ISBN.set("PR6039.032 L67 1954, vol.1")
                        genre.set("FANTASY, ADVENTURE")
                        releasedate.set("29 JULY 1954")
                        bookprice.set("1200.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Lord of the rings.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "MALORIE"):
                        booktitle.set("MALORIE")
                        author.set("JOSH MALERMAN")
                        ISBN.set("9780593156858")
                        genre.set("HORROR, SCI-FICTION, THRILLER")
                        releasedate.set("JUL 21, 2020")
                        bookprice.set("700.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Malorie.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "MASSACRE AT THE PALACE"):
                        booktitle.set("MASSACRE AT THE PALACE")
                        author.set("JONATHAN GREGSON")
                        ISBN.set("978-0786868780")
                        genre.set("HISTORY")
                        releasedate.set("JUNE 5, 2002")
                        bookprice.set("600.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Massacre at the palace.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "MAYUR TIMES"):
                        booktitle.set("MAYUR TIMES")
                        author.set("NARAYAN WAGLE")
                        ISBN.set("9789937829007")
                        genre.set("NOVEL, FICTION")
                        releasedate.set("2010")
                        bookprice.set("400.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Mayur Times.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "MUNA MADAN"):
                        booktitle.set("MUNA MADAN")
                        author.set("LAXMI PRASAD DEVKOTA")
                        ISBN.set("! NOT AVAILABLE")
                        genre.set("EPIC POETRY")
                        releasedate.set("! NOT AVAILABLE")
                        bookprice.set("200.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Muna madan.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "ONE NIGHT AT CALL CENTRE"):
                        booktitle.set("ONE NIGHT @ CALL CENTRE")
                        author.set("CHETAN BHAGAT")
                        ISBN.set("81-291-0818-6 (Paperback edition)")
                        genre.set("FICTION")
                        releasedate.set("OCTOBER 5, 2005")
                        bookprice.set("400.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\One night at call centre.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "PALPASA CAFE"):
                        booktitle.set("PALPASA CAFE")
                        author.set("NARAYAN WAGLE")
                        ISBN.set("978-9-93-780210-9")
                        genre.set("NOVEL, FICTION")
                        releasedate.set("2005")
                        bookprice.set("330.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Palpasa cafe.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "PRAYOGSALA"):
                        booktitle.set("PRAYOGSALA")
                        author.set("SUDHEER BAHADUR SHARMA")
                        ISBN.set("9789937878906")
                        genre.set("HISTORY")
                        releasedate.set("2013")
                        bookprice.set("360.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Prayogsala.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "SAAYA"):
                        booktitle.set("SAAYA")
                        author.set("SUBIN BHATTARAI")
                        ISBN.set("9789937887779")
                        genre.set("ROMANCE NOVEL")
                        releasedate.set("2014")
                        bookprice.set("250.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Saya.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "SETO DHARTI"):
                        booktitle.set("SETO DHARTI")
                        author.set("AMAR NEUPANE")
                        ISBN.set("978-9937-8563-4-8")
                        genre.set("FICTION")
                        releasedate.set("MARCH 2012")
                        bookprice.set("385.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Seto dharti.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "SHRISH KO FUL"):
                        booktitle.set("SHRISHKO FUL")
                        author.set("PARIJAT")
                        ISBN.set("9993340995")
                        genre.set("NOVEL")
                        releasedate.set("1964")
                        bookprice.set("200.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Srish ko ful.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "STEVE JOBS"):
                        booktitle.set("STEVE JOBS")
                        author.set("WALTER ISAACSON")
                        ISBN.set("1-4516-4853-7")
                        genre.set("BIOGRAPHY")
                        releasedate.set("OCTOBER 24, 2011")
                        bookprice.set("900.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Steve jobs.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "SUMMER LOVE"):
                        booktitle.set("SUMMER LOVE")
                        author.set("SUBIN BHATTARAI")
                        ISBN.set("9789937856386")
                        genre.set("LOVE STORY, NOVEL")
                        releasedate.set("2012")
                        bookprice.set("250.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Summer love.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "THE ONLY GOOD INDIANS"):
                        booktitle.set("THE ONLY GOOD INDIANS")
                        author.set("STEPHEN GRAHAM JONES")
                        ISBN.set("9781982136475")
                        genre.set("THILLER, HORROR")
                        releasedate.set("JULY 14, 2020")
                        bookprice.set("900.00")
                        availability.set("! NOT AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\The only good indians.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "THE RETURN OF THE KING"):
                        booktitle.set("THE RETURN OF THE KING")
                        author.set("J. R. R. TOLKIEN")
                        ISBN.set("PR6039.O32 L6 1954, v.3")
                        genre.set("FANTASY")
                        releasedate.set("20 OCTOBER 1955")
                        bookprice.set("870.00")
                        availability.set("!NOT AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\The return of the king.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "THE UNSPOKEN NAME"):
                        booktitle.set("THE UNSPOKEN NAME")
                        author.set("A.K. LARKWOOD")
                        ISBN.set("1250238900")
                        genre.set("FANTASY,SCI-FI")
                        releasedate.set("11 FEB 2020")
                        bookprice.set("950.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\The unspoken name.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "THE WINDS OF WINTER"):
                        booktitle.set("THE WINDS OF WINTER")
                        author.set("GEORGE R. R. MARTIN")
                        ISBN.set("----------")
                        genre.set("EPIC FANTASY")
                        releasedate.set("----")
                        bookprice.set("1100.00")
                        availability.set("!NOT AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\TheWindsofWinter.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)

                    elif (search == "TWO STATES"):
                        booktitle.set("2 STATES")
                        author.set("CHETAN BHAGAT")
                        ISBN.set("978-81-291-1530-0")
                        genre.set("FICTION, ROMANCE")
                        releasedate.set("OCTOBER 8, 2009")
                        bookprice.set("400.00")
                        availability.set("AVAILABLE")
                        self.image = PhotoImage(file="frontend\\Picture\Book PNGs\Two States.png")
                        self.P_lbl = Label(bookdetail, image=self.image)
                        self.P_lbl.place(x=95, y=10)
                else:
                    tkinter.messagebox.showerror("Error", "Book not found !")
                    self.txtsearch.focus()
            else:
                tkinter.messagebox.showerror("Error", "Please enter book name !")
                self.txtsearch.focus()

        self.Search_icon = PhotoImage(file="frontend\\Picture\Icons\Search.png")

        self.txtsearch = Entry(root, relief=GROOVE, bg="#949690", fg="Black", font=('times', 10, 'bold'),
                               textvariable=search)
        self.txtsearch.place(x=975, y=100, width=215)

        # *************************BOOK LISTBOX************************

        scrollbar = Scrollbar(bookframe)
        scrollbar.grid(row=0, column=1, sticky='ns')

        ListOfBox = ['A CLASH OF KINGS', 'A DREAM OF SPRING', 'ARRESTTING GOD IN KTM', 'CHINA HARAYEKO MANCHE',
                     'FIVE POINT SOMEONE', 'GAME OF THRONES', 'THE GIRL IN ROOM 105',
                     'HALF GIRLFRIEND', 'INDIA AFTER GANDHI', 'INTO THE WILD', 'JIWAN KADA KI FUL', 'KARNALI BLUES',
                     'LORD OF THE RING', 'MALORIE', 'MASSACRE AT THE PALACE',
                     'MAYUR TIMES', 'MUNA MADAN', 'ONE NIGHT AT CALL CENTRE', 'PALPASA CAFE', 'PRAYOGSALA',
                     'SAAYA', 'SETO DHARTI', 'SHRISH KO FUL', 'STEVE JOBS', 'SUMMER LOVE', 'THE ONLY GOOD INDIANS',
                     'THE RETURN OF THE KING', 'THE UNSPOKEN NAME',
                     'THE WINDS OF WINTER', 'TWO STATES']

        booklist = Listbox(bookframe, bg="black", fg="#079296", width=28, height=26, font=('times', 9, 'bold'))
        booklist.grid(row=0, column=0, padx=2)
        scrollbar.config(command=booklist.yview)

        for items in ListOfBox:
            booklist.insert(END, items)

        # ************************BUTTON*****************************
        self.btnsearch = Button(root, image=self.Search_icon, text='      Search ', font=('times', 10, 'bold'),
                                bg="#10b5e5", compound=LEFT, fg="black", height=13, width=7, bd=2, relief=GROOVE,
                                command=lambda: Search_Btn(ListOfBox, self.txtsearch.get()))
        self.btnsearch.place(x=1199, y=99, width=110)
        self.root.bind("<Return>", lambda event: Search_Btn(ListOfBox, self.txtsearch.get()))

        self.btn_done = Button(c_detail, text='Done', font=('times', 10, 'bold'), bg="#5cb85c", fg="white", width=7,
                               bd=2, relief=GROOVE, command=lambda: done(self.txtfirstname.get(),
                                                                         self.txtsurname.get(), self.txtaddress.get(),
                                                                         self.txtmobile_no.get(), self.txtemail.get(),
                                                                         self.txt_date.get(), self.txt_Booktitle.get(),
                                                                         self.txtPrice.get(), self.txtqty.get(),
                                                                         self.txtdiscount.get()))
        self.btn_done.place(x=80, y=490)

        self.btn_clear = Button(c_detail, text='Clear', font=('times', 10, 'bold'), bg="#db2020", fg="white", width=7,
                                bd=2, relief=GROOVE, command=iclear)
        self.btn_clear.place(x=220, y=490)

        self.btn_reset = Button(bookdetail, text='Reset', font=('times', 10, 'bold'), bg="#db2020", fg="white", width=7,
                                bd=2, relief=GROOVE, command=ireset)
        self.btn_reset.place(x=200, y=460)

        self.btn_add = Button(bookdetail, image=self.Add_icon, text='Add Book', font=('times', 10, 'bold'),
                              compound=LEFT, bg="#5cb85c", fg="white", width=70, height=18, bd=2, relief=GROOVE,
                              command=bookadd)
        self.btn_add.place(x=60, y=460)
