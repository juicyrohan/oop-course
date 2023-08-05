class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):
        print()

account1 = BankAccount('Bob', 100000, 234324332421)


### HW

#1

class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}', f'Возраст: {self.__age}', f'Направление: {self.__branch}', sep='\n')

    def access_private_method(self):
        self.__display_details()


obj = Student('Adam Smith', 25, 'Information Technology')
obj.access_private_method()


#2

class PizzaMaker:
    def __make_pepperoni(self):
        print('Make pepperoni')

    def _make_barbeque(self):
        print('Make barbeque')

maker = PizzaMaker()

maker._make_barbeque()
#maker.__make_pepperoni()
#print(dir(maker))
#print(PizzaMaker.__dict__.keys())
maker._PizzaMaker__make_pepperoni()



