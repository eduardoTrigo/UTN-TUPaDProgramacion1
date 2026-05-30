print("\n---------Ejercicio 9-------------\n")

agenda = {
    ("lunes", "10:00"): "Clase de programación",
    ("martes", "15:00"): "Reunión de estudio",
    ("viernes", "18:00"): "Entrega de práctico"
}

print("9) consulta de agenda")

dia = input("Ingrese el dia: ").lower()
hora = input("Ingrese la hora, por ejemplo 10:00: ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad registrada en ese dia y horario.")

print("\n---------Ejercicio 9-------------\n")

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("\n10) Diccionario original:")
print(paises_capitales)

print("Diccionario invertido:")
print(capitales_paises)