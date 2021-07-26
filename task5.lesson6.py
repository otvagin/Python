class Stationery:
    _msg = "Запуск отрисовки."
    def draw(self):
        print(self._msg)
class Pen(Stationery):
    title = 'Ручка'
    _msg = f"{title} пишет чернилами."
class Pencil(Stationery):
    title = 'Карандаш'
    _msg = f"{title} рисует графитом."
class Handle(Stationery):
    title = 'Маркер'
    _msg = f"{title} содержит краситель."
Stationery_list = [Pen(), Pencil(), Handle()]
for el in Stationery_list:
    el.draw()
    