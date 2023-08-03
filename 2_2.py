class Cat:

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('hello new object is ', self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

### HW

#1

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

#2

class SoccerPlayer:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

#3

class Zebra:
    def __init__(self):
        self.counter = 0

    def which_stripe(self):
        if self.counter % 2 < 0.5:
            result = 'Полоска белая'
        else:
            result = 'Полоска черная'
        self.counter += 1
        print(result)

#4

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self, crit_age=18):
        if self.age < crit_age:
            return False
        return True


