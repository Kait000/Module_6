class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    __model = None
    __engine_power = None
    __color = None

    def __init__(self, model, color, engine_power):
        Vehicle.__model = model
        Vehicle.__engine_power = engine_power
        Vehicle.__color = color

    def print_info(self):
        return print(self.get_model() + self.get_horsepower() +
                     self.get_color() + 'Владелец:', self.owner)

    def get_model(self):
        return f'Модель: {self.__model}\n'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}\n'

    def get_color(self):
        return f'Цвет: {self.__color}\n'

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на', new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        super().__init__(model, color, engine_power)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
