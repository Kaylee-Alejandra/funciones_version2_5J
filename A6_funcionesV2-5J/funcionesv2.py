print("funciones version 2 ")
print("kaylee luevano")
# zona de listas tuplas, conjuntos o sets y diccionario
#lista
celulares = ["samsung a52"," iphone 11", " chafa"]
# tuplas
maquillaje = ("labial", "rimen", "rubor")
#sets
mikasa = {"mi apa", "mi tia", "yo"}
#diccionario
sisoy = {
    "nombre": "Kaylee",
    "apellido": "Luevano",
    
}
print(sisoy)

# Zona de funciones
def verlista(telefono):
    for uncelular in telefono:
        print(uncelular)

def vertup(mascota):
    for uno in mascota:
        print(uno)

def verset(family):
    for persona in family:
        print(persona)

def verdic(datos):
    for yo in datos:
        print(yo)

# Llamada de funciones
print("imprime celulares de una lista")
verlista(celulares)
vertup(maquillaje)
verset(mikasa)
verdic(sisoy)
