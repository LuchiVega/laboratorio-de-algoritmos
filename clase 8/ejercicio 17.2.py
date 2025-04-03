animal_0 = {"especie:": "gato", "nombre:": "mamau", "dueño": "fabri"}
animal_1 = {"especie:": "perro", "nombre:": "coco", "dueño:": "luchi"}
animal_2 = {"especie:": "perro", "nombre:": "lili", "dueño:": "luchi"}
mascotas = [animal_0, animal_1, animal_2]

for mascota in mascotas:
    for key, value in mascota.items():
        print(key, value)