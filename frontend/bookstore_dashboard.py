from tkinter import *
from tkinter import ttk
from tkinter import Menu
from PIL import Image, ImageTk
import tkinter.messagebox


class Bookstore:

    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Book Store Management System")
        self.root.geometry("1366x778+0+0")
        self.root.iconbitmap("frontend\\Picture\Icons\Icon.ico")

        self.image = Image.open("frontend\\Picture\Picture2.jpg")
        self.photo = ImageTk.PhotoImage(self.image)

        lbl = Label(self.root, image=self.photo)
        lbl.pack(pady=0, padx=0)

        self.Add_icon = PhotoImage(file="frontend\\Picture\Icons\Add.png")

        # *********************COMMAND************************
        # ****************************************************
        def done(firstname, surname, address, mobile_num, email, date, Booktitle, price, quantity, discountount):
            if len(firstname) != 0 and len(surname) != 0 and len(address) != 0 and len(mobile_num) != 0 and len(
                    email) != 0 and len(date) != 0 and len(Booktitle) != 0 and len(price) != 0 and len(
                    quantity) != 0 and len(discountount) != 0:
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
                self.txtdiscountount.focus()
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

        # *******************************COMMAND END****************************
        # *********************************************************************

        # *******************************MENU************************************

        self.menu = Menu(self.root)
        self.file_new_item = Menu(self.menu)
        # self.file_new_item.add_separator()
        self.file_new_item.add_command(label='Edit System Profile')
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

        Title = Label(self.root, text="   C u s t o m e r   D e t a i l   ", font=("akaPosse", 20, "bold"), bg="black",
                      fg="#c97e21", relief=GROOVE)
        Title.place(x=50, y=35)

        Title = Label(self.root, text="B o o k  G e n r e", font=("akaPosse", 20, "bold"), bg="black", fg="#c97e21",
                      relief=GROOVE)
        Title.place(x=495, y=35)

        Title = Label(self.root, text="     B o o k s     ", font=("akaPosse", 20, "bold"), bg="black", fg="#c97e21",
                      relief=GROOVE)
        Title.place(x=715, y=35)

        Title = Label(self.root, text="    B o o k s   D e t a i l    ", font=("akaPosse", 20, "bold"), bg="black",
                      fg="#c97e21", relief=GROOVE)
        Title.place(x=970, y=35)

        # ************************WIDGET**CUSTOMER DETAIL****************************

        self.lblTitle = Label(root, font=('times', 10, 'bold'), text="Title             :", bg="black", fg="white")
        self.lblTitle.place(x=55, y=100)

        self.cboTitle = ttk.Combobox(root, state='readonly', font=('times', 10, 'bold'), textvariable=title)
        self.cboTitle['value'] = ('', 'Mr.', 'Miss.', 'Mrs.', 'Dr.', 'Capt.', 'Ms.')
        self.cboTitle.place(x=170, y=100)

        self.lblfirstname = Label(root, font=('times', 10, 'bold'), text="Firstname   :", bg="black", fg="white")
        self.lblfirstname.place(x=55, y=140)
        self.txtfirstname = Entry(root, textvariable=firstname)
        self.txtfirstname.place(x=170, y=140, width=162)

        self.lblsurname = Label(root, font=('times', 10, 'bold'), text="Surname     :", bg="black", fg="white")
        self.lblsurname.place(x=55, y=180)
        self.txtsurname = Entry(root, textvariable=surname)
        self.txtsurname.place(x=170, y=180, width=162)

        self.lbladdress = Label(root, font=('times', 10, 'bold'), text="Address       :", bg="black", fg="white")
        self.lbladdress.place(x=55, y=220)
        self.txtaddress = Entry(root, textvariable=address)
        self.txtaddress.place(x=170, y=220, width=162)

        self.lblmobile_no = Label(root, font=('times', 10, 'bold'), text="Mobile no.    :", bg="black", fg="white")
        self.lblmobile_no.place(x=55, y=260)
        self.txtmobile_no = Entry(root, textvariable=mobile)
        self.txtmobile_no.place(x=170, y=260, width=162)

        self.lblemail = Label(root, font=('times', 10, 'bold'), text="Email            :", bg="black", fg="white")
        self.lblemail.place(x=55, y=300)
        self.txtemail = Entry(root, textvariable=email)
        self.txtemail.place(x=170, y=300, width=162)

        self.lbl_date = Label(root, font=('times', 10, 'bold'), text="Date              :", bg="black", fg="white")
        self.lbl_date.place(x=55, y=340)
        self.txt_date = Entry(root, textvariable=date)
        self.txt_date.place(x=170, y=340, width=162)

        self.lbl_Booktitle = Label(root, font=('times', 10, 'bold'), text="Book Title   :", bg="black", fg="white")
        self.lbl_Booktitle.place(x=55, y=380)
        self.txt_Booktitle = Entry(root, textvariable=Booktitle)
        self.txt_Booktitle.place(x=170, y=380, width=162)

        self.lblPrice = Label(root, font=('times', 10, 'bold'), text="Price (NPR):", bg="black", fg="white")
        self.lblPrice.place(x=55, y=420)
        self.txtPrice = Entry(root, textvariable=price)
        self.txtPrice.place(x=170, y=420, width=162)

        self.lblqty = Label(root, font=('times', 10, 'bold'), text="Quantity      :", bg="black", fg="white")
        self.lblqty.place(x=55, y=460)
        self.txtqty = Entry(root, textvariable=quantity)
        self.txtqty.place(x=170, y=460, width=162)

        self.lbldiscountount = Label(root, font=('times', 10, 'bold'), text="discountount      :", bg="black",
                                     fg="white")
        self.lbldiscountount.place(x=55, y=500)
        self.txtdiscountount = Entry(root, textvariable=discountount)
        self.txtdiscountount.place(x=170, y=500, width=162)

        # ************************BOOK GENRE***************************
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
        def Search_Btn(search):
            if (len(search) == 0):
                tkinter.messagebox.showerror("Book Store Management System ", "Please enter something !")
                self.txtsearch.focus()
                return
            else:
                tkinter.messagebox.showinfo("Book Store Management System", "Searching......")
                return

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



        # ************************BUTTON*****************************
        self.btnsearch = Button(root, image=self.Search_icon, text='      Search ', font=('times', 10, 'bold'),
                                bg="#10b5e5", compound=LEFT, fg="black", height=13, width=7, bd=2, relief=GROOVE,
                                command=lambda: Search_Btn(self.txtsearch.get()))
        self.btnsearch.place(x=1199, y=99, width=110)

        self.btnsignup = Button(root, text='Done', font=('times', 10, 'bold'), bg="#5cb85c", fg="white", width=7, bd=2,
                                relief=GROOVE, command=lambda: done(self.txtfirstname.get(),
                                                                    self.txtsurname.get(), self.txtaddress.get(),
                                                                    self.txtmobile_no.get(), self.txtemail.get(),
                                                                    self.txt_date.get(), self.txt_Booktitle.get(),
                                                                    self.txtPrice.get(), self.txtqty.get(),
                                                                    self.txtdiscountount.get()))
        self.btnsignup.place(x=150, y=610)

        self.btnsignup = Button(root, text='Clear', font=('times', 10, 'bold'), bg="#db2020", fg="white", width=7, bd=2,
                                relief=GROOVE, command=iclear)
        self.btnsignup.place(x=290, y=610)

        self.btnsignup = Button(bookdetail, text='Reset', font=('times', 10, 'bold'), bg="#db2020", fg="white", width=7,
                                bd=2, relief=GROOVE, command=ireset)
        self.btnsignup.place(x=200, y=460)

        self.btnsignup = Button(bookdetail, image=self.Add_icon, text='Add Book', font=('times', 10, 'bold'),
                                compound=LEFT, bg="#5cb85c", fg="white", width=70, height=18, bd=2, relief=GROOVE,
                                command=bookadd)
        self.btnsignup.place(x=60, y=460)