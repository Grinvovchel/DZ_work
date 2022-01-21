class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationary):
    def draw(self):
        print('Рисуем ручкой', self.title)

class Pencil(Stationary):
    def draw(self):
        print('Рисуем карандашом', self.title)
class Handle(Stationary):
    def draw(self):
        print('Рисуем маркером', self.title)
if __name__ == "__main__":
    pn= Pen('Bic')
    p1= Pencil('Сакко и Ванцети')
    h1 = Handle('Flip Chart')

    pn.draw()
    p1.draw()
    h1.draw()