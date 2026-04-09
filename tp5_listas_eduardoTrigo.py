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
