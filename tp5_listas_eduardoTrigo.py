#ejercicio 1
notas = []

for i in range(10):
    nota = input(f"ingrese la nota {i + 1}  del estudiante: ")
    while not nota.isdigit():
        nota = input("la nota debe ser de valor numerico (1 al 10)")
    notas.append(int(nota))

suma = 0
for i in range(len(notas)):
    suma += notas[i]

promedio = suma / len(notas)

nota_max = notas[0]
nota_min = notas[0]

for i in range(len(notas)):
    if notas[i] > nota_max:
        nota_max = notas[i]
    elif notas[i] < nota_min:
        nota_min = nota[i]

print("Lista de notas:")
for i in range(len(notas)):
    print(f"Nota {i+1} : {notas[i]}")
print(f"promedios: {promedio}")
print(f"La nota más alta es: {nota_max}")
print(f"La nota más baja es: {nota_min}")

#ejercicio 2
productos = []

for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    while not producto.isalpha():
        producto = input(f"Ingrese un nombre del producto {i + 1} valido (solo letras):")
    productos.append(producto)
#la funcion sorted() devuelve una nueva lista ordenada
ordenados = sorted(productos)

print("\nLista de productos ordenada: ")
for i in range(len(ordenados)):
    print(f"producto {i + 1} : {ordenados[i]}")

eliminar = input("Que producto desea eliminar?: ")

if eliminar in ordenados:
    ordenados.remove(eliminar)
    print("\nLista de productos actualizada: ")
    for i in range(len(ordenados)):
        print(f"producto {i + 1} : {ordenados[i]}")
else:
    print("el producto no se encuentra en la lista")


# ejercicio 3
import random

numeros = []

for i in range(15):
    numero = random.randint(1, 100)
    numeros.append(numero)

for i in range(len(numeros)):
    print(f"numero {i+1}: {numeros[i]}")

pares = []
impares = []
cant_pares = 0
cant_impares = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
        cant_pares += 1
    else: 
        impares.append(numeros[i])
        cant_impares += 1

print(f"\nCantidad de numeros pares: {cant_pares}")
for i in range(len(pares)):
    print(pares[i])
print(f"\nCantidad de numeros impares: {cant_impares}")
for i in range(len(impares)):
    print(impares[i])


#ejercicio 4
datos = [1 , 3 , 5 , 3 , 7 , 1 , 9 , 5 , 3]

sin_repetir = []

for i in range(len(datos)):
    if datos[i] not in sin_repetir:
        sin_repetir.append(datos[i])

print("Lista sin repetidos:")
for i in range(len(sin_repetir)):
    print(f"indice {i} : {sin_repetir[i]}")


# ejercicio 5
alumnos_presentes = []

for i in range(8):
    nombre_alumno = input(f"ingrese el nombre del alumno {i+1} presente: ")
    while not nombre_alumno.isalpha():
        nombre_alumno = input(f"ingrese nuevamente el nombre del alumno {i+1} presente: ")
    alumnos_presentes.append(nombre_alumno)

print(f"\nListado de alumnos presentes: ")
for i in range(len(alumnos_presentes)):
    print(f"alumno {i + 1} : {alumnos_presentes[i]}")

salir = False

while not salir:
    print("\nElija una opcion: ")
    print("1) Eliminar alumno.")
    print("2) Agregar alumno.")
    print("3) Salir.")
    opcion = input()
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Ingrese una opcion 1 al 3:")

    if opcion == "1":
        eliminar = input("Ingrese el nombre del alumno para sacarlo de la lista")
        while not eliminar.isalpha():
            eliminar = input(f"Ingrese nuevamente el nombre del alumno a eliminar: ")
        alumnos_presentes.remove(eliminar)
    elif opcion == "2":
        agregar = input("Ingrese el nombre del alumno para agregar a la lista")
        while not agregar.isalpha():
            agregar = input("Ingrese nuevamente el nombre del alumno para agregar a la lista")
        alumnos_presentes.append(agregar)
    elif opcion == "3":
        print("Saliendo...")
        salir = True
        break
    print(f"\nListado de alumnos presentes: ")
    for i in range(len(alumnos_presentes)):
        print(f"alumno {i + 1} : {alumnos_presentes[i]}")

#ejercicio 6
numeros = []

for i in range(7):
    numero = input("Ingrese un numero (del 1 al 10): ")
    while not numero.isdigit():
        numero = input("Ingrese nuevamente un numero valido del 1 al 10: ")
    numeros.append(numero)

print("\nLista numeros: ")
for i in range(len(numeros)):
    print(f"numero{i + 1} : {numeros[i]}")

ultimo = numeros[-1]
numeros = [ultimo] + numeros[:-1]

print("\nLista numeros invertida: ")
for i in range(len(numeros)):
    print(f"numero{i} : {numeros[i]}")

#ejercicio 7
temperaturas = []

for i in range(7):
    print(f"\nDia: {i + 1}")
    temp_min = float(input("ingrese la temperatura minima del dia: "))
    temp_max = float(input("ingrese la temperatura maxima del dia: "))
    while temp_max < temp_min:
        temp_max = float(input("Ingrese una máxima mayor o igual a la mínima: "))

    temperaturas.append([temp_min, temp_max])

suma_min = 0
suma_max = 0

for i in range(len(temperaturas)):
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]

prom_min = suma_min / len(temperaturas)
prom_max = suma_max / len(temperaturas)

mayor_amplitud = float('-inf')
dia_mayor = 0

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]

    if mayor_amplitud < amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i +1

print(f"Día con mayor amplitud térmica: {dia_mayor} , amplitud: {mayor_amplitud}" )

#ejercicio 8

notas = []

for i in range(5):
    fila = []
    print(f"\nEstudiante {i + 1}: ")
    for j in range(3):
        nota = input(f"ingrese la nota {j + 1}: ")
        while not nota.isdigit() or int(nota) < 0 or int(nota) > 10:
            nota = input("ingrese una nota valida del 0 al 10: ")
        fila.append(int(nota))
    notas.append(fila)

lista_promedios = []

for i in range(5):
    suma = 0        
    for j in range(3):
        suma += notas[i][j]
    
    promedio = suma / 3
    lista_promedios.append(promedio)


print("\nPromedio por alumno: ")
for i in range(len(lista_promedios)):
    print(f"alumno {i + 1} : {lista_promedios[i]:.2f}")


print("\nPromedio por materia:")

for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    
    promedio = suma / 5
    print(f"Materia {j+1}: {promedio:.2f}")


# ejercicio 9
tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

turno = "X"
jugada = 0

while jugada < 9:
    print("\nTablero:")
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end= " ")
        print()

    print(f"\nTurno de : {turno}")

    fila = input("ingrese fila del 1 al 3: ")
    while not fila.isdigit() or int(fila) < 1 or int(fila) > 3:
        fila = input("ingrese fila del 1 al 3: ") 
    
    columna = input("ingrese fila del 1 al 3: ")
    while not fila.isdigit() or int(columna) < 1 or int(columna) > 3:
        columna = input("ingrese fila del 1 al 3: ") 
    
    fila = int(fila)
    columna = int(columna)

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = turno
        jugada += 1

        if turno == "X":
            turno = "O"
        else:
            turno = "X"
    else:
        print("Esa posición ya está ocupada, intentá de nuevo")

print("\nTablero final:")
for i in range(3):
    for j in range(3):
        print(tablero[i][j], end=" ")
    print()

#ejercicio 10:
cant_productos = 4
cant_dias = 7

ventas = []

for i in range(cant_productos):
    fila = []
    print(f"\nProducto {i + 1}: ")
    for j in range(cant_dias):
        venta = input(f"ingrese la venta del dia {j + 1} :")
        while not venta.isdigit() or int(venta) < 0:
            venta = input(f"Ingrese un número válido mayor o igual a 0 :")
        fila.append(int(venta))
    ventas.append(fila)

print("\nTotal vendido por cada producto:")
total_ventas = []

for i in range(cant_productos):
    suma = 0
    for j in range(cant_dias):
        suma += ventas[i][j]
    total_ventas.append(suma)
    print(f"Producto {i+1}: {suma}")

mayor_ventas_dia = float('-inf')
dia_mayor = 0

for j in range(cant_dias):
    suma = 0
    
    for i in range(cant_productos):
        suma += ventas[i][j]
    
    if suma > mayor_ventas_dia:
        mayor_ventas_dia = suma
        dia_mayor = j + 1

print(f"\nDía con mayores ventas: Día {dia_mayor}")

mayor_producto = float('-inf')
producto_mayor = 0

for i in range(cant_productos):
    if total_ventas[i] > mayor_producto:
        mayor_producto = total_ventas[i]
        producto_mayor = i + 1

print(f"Producto más vendido en la semana: Producto {producto_mayor}")
