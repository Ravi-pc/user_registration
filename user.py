"""
@Author: Ravi Singh

@Date: 2023-20-12 10:20:30

@Last Modified by:

@Last Modified time: 2023-20-12 14:20:30

@Title : User Registration Form
"""

import re


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = email

    def name_validation(self):
        check = re.compile(r'^[A-Z][a-zA-Z]{2,}$')
        if check.match(self.first_name) and check.match(self.last_name):
            return True
        else:
            return False

    def email_validation(self):
        check = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        if check.match(self.e_mail):
            return True
        else:
            return False


if __name__ == '__main__':
    f_name = input('Enter First Name\n')
    l_name = input('Enter Last Name\n')
    e_mail = input('Enter E-Mail\n')
    user_obj = User(f_name, l_name, e_mail)
    print(user_obj.name_validation())
    print(user_obj.email_validation())
