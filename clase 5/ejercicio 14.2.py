user = []

for usuario in user:
    if usuario == "admin":
        print("bienvenido admin quiere ver un informe de estado")
    else:
        print("hola", usuario, "gracias por iniciar sesion")
else:
    print("¡Necesitamos mas usuarios!")