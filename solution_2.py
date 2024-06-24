# Задание 2: Автоматизация управления теплицей (Инкапсуляция)

class Greenhouse:
    def __init__(self):
        self._temperature = 20  # начальная температура
        self._humidity = 50     # начальная влажность
        self._light_level = 100 # начальный уровень света

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if 15 <= value <= 30:
            self._temperature = value
        else:
            raise ValueError("Temperature must be between 15 and 30 degrees.")

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        if 40 <= value <= 70:
            self._humidity = value
        else:
            raise ValueError("Humidity must be between 40 and 70 percent.")

    @property
    def light_level(self):
        return self._light_level

    @light_level.setter
    def light_level(self, value):
        if 0 <= value <= 100:
            self._light_level = value
        else:
            raise ValueError("Light level must be between 0 and 100 percent.")

greenhouse = Greenhouse()

print("Initial temperature:", greenhouse.temperature)
greenhouse.temperature = 25
print("New temperature:", greenhouse.temperature)

try:
    greenhouse.temperature = -5
except ValueError as e:
    print(e)

try:
    greenhouse.temperature = 50
except ValueError as e:
    print(e)
