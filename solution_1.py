# Задание 1: Управление фонтанами (Полиморфизм)

class Fountain:
    def spray_water(self):
        raise NotImplementedError

class SimpleFountain(Fountain):
    def spray_water(self):
        print("Simple Fountain is spraying water.")

class MusicalFountain(Fountain):
    def spray_water(self):
        print("Musical Fountain is playing a symphony with water.")

class LightedFountain(Fountain):
    def spray_water(self):
        print("Lighted Fountain is dancing with lights and water.")

fountains = [
    SimpleFountain() for _ in range(1)
] + [
    MusicalFountain(),
    LightedFountain()
]

for fountain in fountains:
    fountain.spray_water()
