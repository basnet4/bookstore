class Book:
    def __init__(self, booktitle, author, isbn, genre, release_date, price, availability):
        self.__booktitle = booktitle
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__release_date = release_date
        self.__price = price
        self.__availability = availability

    def set_booktitle(self, booktitle):
        self.__booktitle = booktitle

    def get_booktitle(self):
        return self.__booktitle

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn

    def set_genre(self, genre):
        self.__genre = genre

    def get_genre(self):
        return self.__genre

    def set_release_date(self, release_date):
        self.__release_date = release_date

    def get_release_date(self):
        return self.__release_date

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_availability(self, availability):
        self.__availability = availability

    def get_availability(self):
        return self.__availability
