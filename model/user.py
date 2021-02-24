class User:
    def __init__(self, firstname, surname, username, password, mobile, dob, gender):
        self.__firstname = firstname
        self.__surname = surname
        self.__username = username
        self.__password = password
        self.__mobile = mobile
        self.__dob = dob
        self.__gender = gender

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def get_firstname(self):
        return self.__firstname

    def set_surname(self, surname):
        self.__surname = surname

    def get_surname(self):
        return self.__surname

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_mobile(self, mobile):
        self.__mobile = mobile

    def get_mobile(self):
        return self.__mobile

    def set_dob(self, dob):
        self.__dob = dob

    def get_dob(self):
        return self.__dob

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender
