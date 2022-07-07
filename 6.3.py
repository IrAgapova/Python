class Worker:
    def __init__(self, name, surname, position, wage, bonus ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit":wage, "bonus":bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return sum(self._income.values())
po_1 = Position("Павел", "Иванов", "сварщик", 4444, 1200000)
print(po_1.get_full_name( ))







