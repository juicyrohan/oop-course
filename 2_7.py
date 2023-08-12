###HW

#1

class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        n = 1
        for note in self._notes:
            print(f'{n}. {note}')
            n += 1

note = Notebook(['Buy potato', 'Buy carrot', 'Wash car'])
note.notes_list

#2

class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if value > 0 and isinstance(value, int):
            self.total_cents = value * 100 + self.total_cents % 100

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if value > 0 and value < 100 and isinstance(value, int):
            self.total_cents = (self.total_cents // 100) * 100 + value

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'

Bill = Money(101, 99)
print(Bill)
print(Bill.dollars, Bill.cents)
print(Bill.total_cents)
Bill.dollars = 666
print(Bill)
Bill.cents = 12
print(Bill)
