class Cat:
    breed = 'pers'

    def hello(self):
        print('hello world from kitty', self)

    def show_breed(self):
        print(f'My breed is {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'My name is {self.name}')
        else:
            print('No name')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age


### HW
#1

class Lion():

    def roar(self):
        print('Rrrrrrr!')

#2

class Counter():
    def start_from(self, start=0):
        self.counter = start

    def increment(self):
        if hasattr(self, 'counter'):
            self.counter += 1
        else:
            print('Have not started counting yet')

    def display(self):
        if hasattr(self, 'counter'):
            print(f'Текущее значение счетчика = {self.counter}')
        else:
            print('Have not started counting yet')

    def reset(self):
        self.counter = 0

#3

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, point):
        if isinstance(point, Point) and hasattr(self, 'x') and hasattr(self, 'y'):
            if hasattr(point, 'x') and hasattr(point, 'y'):
                dist = ((abs(self.x-point.x))**2 + (abs(self.y-point.y))**2)**0.5
                print(dist)
            else:
                print('Вторая точка не задана')
        else:
            print('Передана не точка')




