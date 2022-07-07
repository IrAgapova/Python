class Stationer:
    def __init__(self, title="Чертеж"):
        self.title=title

    def draw(self):
        print(f"Начинаем рисовать{self.title}")

class Pen(Stationer):
    def draw(self):
        print(f"Рисуем карандашом {self.title}")

class Pencil(Stationer):
    def draw(self):
        print(f"Рисуем ручкой {self.title}")

class Marker(Stationer):
    def draw(self):
        print(f"Рисуем маркером {self.title}")

stat = Stationer()
pen = Pen ("Муравей")
pencil = Pencil ("Оса")
marker = Marker ("Жук")

of_1 = [stat, pen, pencil, marker]

for i in of_1:
    i.draw()
