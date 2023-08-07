### HW

#1

import re

class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        pattern = r'\w+@\w+.[a-z]{2,}'
        if not isinstance(new_email, str) or not re.fullmatch(pattern, new_email):
            print(f'ErrorMail: {new_email}')
        else:
            self.__email = new_email

    email = property(fget=get_email, fset=set_email)

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)
k.email = [1, 2, 3]
k.email = 'prince@still@.wait'
print(k.email)
k.email = 'prince@still.wait'
print(k.email)
