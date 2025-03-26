import random

edad = random.randint(1, 100)
print(edad)

if edad < 2:
    print("Es un bebe")
elif edad >= 2 and edad < 4:
    print("Es un niño")
elif edad >= 4 and edad < 13:
    print("Es un nene")
elif edad >= 13 and edad < 20:
    print("Es un adolescente")
elif edad >= 20 and edad < 65:
    print("Es un adulto")
else:
    print("Es un adulto mayor")