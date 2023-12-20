"""
@Author: Ravi Singh

@Date: 2023-20-12 10:20:30

@Last Modified by:

@Last Modified time: 2023-20-12 14:20:30

@Title : User Registration Form
"""

import re


class User:
    def __init__(self, first_name):
        self.first_name = first_name

    def name_validation(self):
        check = re.compile(r'^[A-Z][a-zA-Z]{2,}$')
        if check.match(self.first_name):
            return True
        else:
            return False


if __name__ == '__main__':
    f_name = input('Enter First Name\n')
    user_obj = User(f_name)
    print(user_obj.name_validation())
