import time

invitados = ["Deyes", "Tomi", "Panchi"]

print (invitados[0],"veni a casa a comer vienen",invitados[1], "y",invitados[2])
time.sleep(1)
print (invitados[1],"veni a casa a comer vienen",invitados[0],"y",invitados[2])
time.sleep(1)
print (invitados[2],"veni a casa a comer vienen",invitados[0],"y",invitados[1])
time.sleep(1)

print (f"Deyes: no puedo estoy en Costa Rica")
time.sleep(1)

invitados.pop(0)

invitados.append("Paro")

print (invitados[2],"veni a casa a comer vienen",invitados[0],"y",invitados[1])
time.sleep(1)

print("Chicos mi mama me dejo invitar a mas")
time.sleep(1)

invitados.insert(0, "Colo")
invitados.insert(1, "Lu")
invitados.append("Faka")

print (invitados[0],"veni a casa a comer vienen los chicos")
time.sleep(1)
print (invitados[1],"veni a casa a comer vienen los chicos")
time.sleep(1)
print (invitados[5],"veni a casa a comer vienen los chicos")
time.sleep(1)