###HW

#1

class Rectangle:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def area(self):
        return self._length * self._width

r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print((r1.area))
print((r2.area))

#2

class Date:

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @property
    def date(self):
        return f'{(2-len(str(self._day)))*"0"}{self._day}/{(2-len(str(self._month)))*"0"}{self._month}/{(4-len(str(self._year)))*"0"}{self._year}'

    @property
    def usa_date(self):
        return f'{(2-len(str(self._month)))*"0"}{self._month}-{(2-len(str(self._day)))*"0"}{self._day}-{(4-len(str(self._year)))*"0"}{self._year}'

d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)


print(d1.date)
print(d1.usa_date)
print(d2.date)
print(d2.usa_date)

