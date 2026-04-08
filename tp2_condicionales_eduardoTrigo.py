#Trigo Estrada Hector Eduardo

#ejercicio 1
edad = int(input("ingrese su edad.\n"))
if edad >= 18:
    print("usted es mayor de edad")
print("fin")

#ejercicio 2
nota = int(input("ingrese su nota.\n"))
if nota >= 6:
    print("estas aprobado.\n")
else: 
    print("estas desaprobado.\n")

#ejercicio 3
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.\n")
else:
    print("Por favor, ingrese un número par.\n")

#ejercicio 4
edad = int(input("ingrese una edad.\n"))
if edad < 12:
    print("es un niño/a")
elif edad >=12 and edad < 18 :
    print("es un adolecente")
elif edad >= 18 and edad < 30:
    print("es un adulto/a joven")
else:
    print("es un adulto mayor")

#ejercicio 5
passw = input("ingrese una contraseña ( de 8 a 14 caracteres)")

if len(passw) >=8 and len(passw)<= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6
consumo = float(input("Ingrese el consumo mensual en kWh: "))

if consumo < 150:
    print("Consumo bajo")
elif consumo >= 150 and consumo <= 300:
    print("Consumo medio")
elif consumo > 300:
    print("Consumo alto")
    if consumo > 500:
        print("Considere medidas de ahorro energético")

#ejercicio 7
frase = input("ingrese una frase: ")
letra_final = frase[-1].lower()
 
if letra_final == "a" or letra_final == "e" or letra_final == "i" or letra_final == "o" or letra_final == "u":
    frase = frase + "!"

print(frase)

#ejercicio 8
nombre = input("ingrese su nombre:\n")
descripcion = ""

opcion = int(input("seleccione una opcion (1, 2 o 3)\n" \
                   "1. Mostrar nombre en mayúsculas.\n" \
                   "2. Mostrar nombre en minúsculas.\n" \
                   "3. Mostrar nombre con la primera letra mayúscula.\n"))
if opcion == 1:
    descripcion = "Texto en Mayusculas: "
    nombre = nombre.upper()
elif opcion == 2:
    descripcion = "Texto en Minusculas: "
    nombre = nombre.lower()
elif opcion == 3:
    descripcion = "Texto con la primera letra en mayúscula: "
    nombre = nombre.title()
else:
    print("seleccion incorrecta")

print(descripcion + nombre)

#ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#ejecicio 10
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

if hemisferio == "N":
    print("Estación:", estacion_norte)
elif hemisferio == "S":
    if estacion_norte == "Invierno":
        print("Estación: Verano")
    elif estacion_norte == "Primavera":
        print("Estación: Otoño")
    elif estacion_norte == "Verano":
        print("Estación: Invierno")
    else:
        print("Estación: Primavera")
else:
    print("Hemisferio inválido")