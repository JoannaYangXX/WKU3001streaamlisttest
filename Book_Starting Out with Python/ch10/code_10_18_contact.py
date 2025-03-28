# code_10_18_contact.py
# The Contact class holds contact information.

class Contact:
    # The __init__ method initializes the attributes.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # The set_name method sets the name attributes.
    def set_name(self, name):
        self.__name = name

    # The set_phone
    def set_phone(self, phone):
        self.__phone = phone

    # The set_email
    def set_email(self, email):
        self.__email = email

    # The get_name method returns the name attribute
    def get_name(self):
        return self.__name

    # The get_phone
    def get_phone(self):
        return self.__phone

    # the get_email
    def get_email(self):
        return self.__email

    # the __str__ method returns the object's state
    def __str__(self):
        return "Name: " + self.__name + \
                "\nPhone: " + self.__phone + \
                "\nEmail: " + self.__email
