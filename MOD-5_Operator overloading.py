
# Домашнее задание по уроку "Перегрузка операторов"



class Building:
    def __init__(self, number_of_floors, building_type):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __str__(self):
        return f'В {self.buildingType} {self.numberOfFloors} этажей'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


devGreen = Building(17, 'ЖК Грин-Сити')
devVnuk = Building(12, 'ЖК Новое-Внуково')

print(devGreen)
print(devGreen == devVnuk)



