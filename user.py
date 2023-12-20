"""
@Author: Ravi Singh

@Date: 2023-20-12 10:20:30

@Last Modified by:

@Last Modified time: 2023-20-12 14:20:30

@Title : User Registration Form
"""

import re


class User:
    def __init__(self, first_name, last_name, email, num, password):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = email
        self.num = num
        self.password = password

    def name_validation(self):
        """
            Description: name_validation function is used to check entered first name and last name
                        is valid or not.

            Parameter: Self as a parameter.

            Return:    True or False

        """
        check = re.compile(r'^[A-Z][a-zA-Z]{2,}$')
        if check.match(self.first_name) and check.match(self.last_name):
            return True
        else:
            return False

    def email_validation(self):
        """
            Description: email_validation function is used to check entered email
                        is valid or not.

            Parameter: Self as a parameter.

            Return:    True or False

        """
        check = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$')
        if check.match(self.e_mail):
            return True
        else:
            return False

    def number_validation(self):
        """
            Description: number_validation function is used to check entered phone number
                        is valid or not.

            Parameter: Self as a parameter.

            Return:    True or False

        """
        check = re.compile(r'^(91 [6-9])[0-9]{9}$')
        if check.match(self.num):
            return True
        else:
            return False

    def password_validation(self):
        """
            Description: password_validation function is used to check entered password is valid or not
                        is valid or not.

            Parameter: Self as a parameter.

            Return:    True or False

        """
        check = re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
        if check.match(self.password):
            return True
        else:
            return False


if __name__ == '__main__':
    f_name = input('Enter First Name\n')
    l_name = input('Enter Last Name\n')
    e_mail = input('Enter E-Mail\n')
    ph_no = input('Enter the Mobile Number\n')
    passwd = input('Enter the Password\n')
    user_obj = User(f_name, l_name, e_mail, ph_no, passwd)
    print(user_obj.name_validation())
    print(user_obj.email_validation())
    print(user_obj.number_validation())
    print(user_obj.password_validation())
