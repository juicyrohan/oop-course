from string import digits, ascii_letters, ascii_uppercase

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        print('get login')
        return self.__login

    @login.setter
    def login(self, value):
        print('set login')
        if '@' not in value:
            raise ValueError("Login must include at least one '@'")
        if '.' not in value:
            raise ValueError("Login must include at least one '.'")
        self.__login = value

    @property
    def password(self):
        print('get password')
        return self.__password

    @staticmethod
    def is_include_digit(value):
        for digit in digits:
            if digit in value:
                return True
        return False

    @staticmethod
    def is_include_all_register(value):
        i = 0
        for letter in value:
            if letter in ascii_uppercase:
                i += 1
            if i == 2:
                return True
        return False

    @staticmethod
    def is_include_only_latin(value):
        for letter in value:
            if letter not in ascii_letters and letter not in digits:
                return False
        return True

    @staticmethod
    def check_password_dictionary(value):
        f = open('easy_passwords.txt', 'r')
        easy_pass = f.read()
        f.close()
        if value in easy_pass:
            return False
        return True

    @password.setter
    def password(self, value):
        print('set password')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 5 or len(value) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и короче 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')

        self.__password = value



reg1 = Registration('Kenobi@mail.ru', 'wddWQw1')
print(reg1.login)
print(reg1.password)
reg1.login = '123@wer.com'




