from Untitled.Car import Car

car_1 = Car(
    'Toyota',
    'Corolla',
    2007,
    'Blue'
)

car_2 = Car(
    'Ford',
    'Mustang',
    2022,
    'Red'
)

car_1.drive()
car_1.stop()

print(car_1.wheels)
print(car_2.wheels)