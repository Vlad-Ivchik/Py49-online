class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    @staticmethod
    def start_auto():
        print('Автомобиль заведён')

    def year_release(self):
        return self.year

    def type_auto(self):
        return self.type

    def color_auto(self):
        return self.color

    @staticmethod
    def stop_auto():
        print('Автомобиль заглушен')


auto = Car('черный', 'легковой', 1993)

auto.start_auto()
print(auto.type_auto())
print(auto.color_auto())
print(auto.year_release())
auto.stop_auto()