lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personas = ["Fabri", "Eduardo", "Luca", "Agustina", "Agus", "Juan", "Sara"]

for persona in personas:
    if persona in lenguajes_favoritos:
        print(persona, "Gracias por responder la encuesta")
    else:
        print(persona, "Te invito a responder una encuesta")