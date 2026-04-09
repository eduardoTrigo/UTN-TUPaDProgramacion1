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