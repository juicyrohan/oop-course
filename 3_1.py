class Person:

    def __init__(self, name, surname, gender='male'):
        self.gender = gender
        self.name = name
        self.surname = surname

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        print('set gender')
        if value in ['male', 'female']:
            self._gender = value
        else:
            print('Не знаю, что вы имели в виду? Пусть это будет мальчик!')
            self._gender = 'male'

    @staticmethod
    def which_citizen(value):
        if value == 'male':
            citizen = 'Гражданин'
        else:
            citizen = 'Гражданка'
        return citizen

    def __str__(self):
        citizen = Person.which_citizen(self.gender)
        return f'{citizen} {self.surname} {self.name}'

p1 = Person('Chuck', 'Norris')
print(p1)
p2 = Person('Mila', 'Kunis', 'female')
print(p2)
p3 = Person('Обиван', 'Кеноби', True)
print(p3)