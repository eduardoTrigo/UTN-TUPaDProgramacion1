# TP 7 - Estructuras de datos complejas

# Ejercicio 1

precios_frutas = {
    "Banana": 1200,
    "Anana": 2500,
    "Melon": 3000,
    "Uva": 1450
}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print("1) Diccionario con frutas agregadas:")
print(precios_frutas)

print("----------------------\n")
#Ejercicio 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

print("2) Diccionario con precios actualizados: ")
print(precios_frutas)

print("\n---------Ejercicio 3-------------\n")
#Ejercicio 3

frutas = list(precios_frutas.keys())

print("3) Lista de frutas sin precios: ")
print(frutas)

print("\n---------Ejercicio 4-------------\n")

contactos = {}

print("4) Carga de Contactos")

for i in range(5):
    nombre = input(f"Ingrese el numero de contacto{i+1}: ")
    telefono = input(f"Ingrese el telefono de {nombre}: ")

    contactos[nombre] = telefono

buscar = input("Ingrese el contacto a buscar: ")

if buscar in contactos:
    print(f"El telefono de {buscar} es {contactos[buscar]}")
else:
    print("Contacto no encontrado")

print("\n---------Ejercicio 5-------------\n")

frase = input("5) Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

cant_palabras = {}

for palabra in palabras:
    cant_palabras[palabra] = cant_palabras.get(palabra, 0) + 1

print("palabras unicas: ")
print(palabras_unicas)

print("Cantidad de apariciones: ")
print(cant_palabras)

print("\n---------Ejercicio 6-------------\n")

alumnos = {}

print("6) Carga de alumnos y notas")

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))

    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedio de notas por alumnos: ")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

print("\n---------Ejercicio 7-------------\n")

asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "pedro", "Ana"]

print("\n7) Lista Original de asistencias: ")
print(asistencias)

empleados_unicos = set(asistencias)

print("Empleados que asistieron al menos una vez:")
print(empleados_unicos)

print("Cantidad de asistencias por empleado:")

for empleado in empleados_unicos:
    cantidad = asistencias.count(empleado)
    print(f"{empleado}: {cantidad} vez/veces") 

print("\n---------Ejercicio 8-------------\n")

stock = {
    "lapiz": 10,
    "cuaderno": 5,
    "goma":3
}

print("Stock Actual: ")
print(stock)

print("8) Gestion de stock")
producto = input("ingrese el producto a consultar o modificar: ")

if producto in stock:
    print(f"stock actual de {producto}: {stock[producto]}")

    unidades = int(input("Ingrese cuantas unidades desea agregar: "))
    stock[producto] += unidades

    print(f"Nuevo Stock de {producto}: {stock[producto]}")
else:
    print("El producto no existe.")

    unidades = int(input("Ingrese el stock inicial del nuevo producto: "))
    stock[producto] = unidades

    print("Producto agregado correctamente.")

print("Stock Actualizado: ")
print(stock)

print("\n---------Ejercicio 9-------------\n")

agenda = {
    ("lunes", "10:00"): "Clase de programación",
    ("martes", "15:00"): "Reunión de estudio",
    ("viernes", "18:00"): "Entrega de práctico"
}

print("9) consulta de agenda")

dia = input("Ingrese el dia: ").lower()
hora = input("Ingrese la hora, por ejemplo 10:00")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad registrada en ese dia y horario.")