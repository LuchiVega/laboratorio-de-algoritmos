persona_0 = {"nombre": "luciano", "apellido": "vega", "edad": 16, "ciudad": "barracas"}
persona_1 = {"nombre": "fabrizio", "apellido": "giordanelli", "edad": 16, "ciudad": "avellaneda"}
persona_2 = {"nombre": "agustin", "apellido": "granes", "edad": 16, "ciudad": "avellaneda"}
personas = [persona_0, persona_1, persona_2]

for persona in personas:
    print("Nombre:", persona["nombre"])
    print("Apellido:", persona["apellido"])
    print("Edad:", persona["edad"])
    print("Ciudad:", persona["ciudad"])