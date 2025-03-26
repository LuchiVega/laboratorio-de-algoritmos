import random

user = ["fabri", "agus", "luca", "admin"]
usuario = random.randint(0,3)

if usuario == 0:
    print("bienvenido", user[0])
elif usuario == 1:
    print("bienvenido", user[1])
elif usuario == 2:
    print("bienvenido", user[2])
else:
    print("bienvenido", user[3],"quiere ver un informe de estado")