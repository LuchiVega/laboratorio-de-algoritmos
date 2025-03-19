import time

invitados = ["Deyes", "Tomi", "Panchi"]

print (invitados[0],"veni a casa a comer vienen",invitados[1], "y",invitados[2])
time.sleep(1)
print (invitados[1],"veni a casa a comer vienen",invitados[0],"y",invitados[2])
time.sleep(1)
print (invitados[2],"veni a casa a comer vienen",invitados[0],"y",invitados[1])
time.sleep(1)

print ("Deyes: no puedo estoy en Costa Rica")
time.sleep(1)

invitados.pop(0)

invitados.append("Paro")

print (invitados[2],"veni a casa a comer vienen",invitados[0],"y",invitados[1])