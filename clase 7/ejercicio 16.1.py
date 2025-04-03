glosario = {
    "lenguaje": "conjunto de reglas e instrucciones que permiten a los programadores comunicarse con una computadora",
    "programar": "acción de crear programas o aplicaciones mediante el desarrollo de un código fuente",
    "lista": "estructura de datos que permite almacenar varios elementos de manera ordenada",
    "diccionario": "estructura de datos que relaciona claves con valores",
    "variable": "es un contenedor que almacena valores de datos",
    "función": "bloque de código diseñado para realizar una tarea específica, que puede ser reutilizado",
    "bucle": "estructura de control que repite un bloque de código varias veces mientras se cumpla una condición",
    "condicional": "estructura de control que permite ejecutar un bloque de código dependiendo de si se cumple una condición",
    "clase": "plantilla para crear objetos, definiendo las propiedades y métodos que tendrán esos objetos",
    "objeto": "instancia de una clase, con propiedades y comportamientos definidos por esa clase"
}

for key, value in glosario.items():
    print (key.title(), value.capitalize())