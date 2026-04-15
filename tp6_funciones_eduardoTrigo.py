# TP funciones

#ejercicio 1:
def imprimir_hola_mundo():
    print("hola mundo..")

imprimir_hola_mundo()

#ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre} ...")

nombre = input("ingrese su nombre: ")

saludar_usuario("Lemmy")

#ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("ingrese su nombre: ")
apellido = input("ahora ingrese su apellido: ")
edad = input("ingrese su edad: ")
residencia = input("ingrese el lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#ejercicio 4
def calcular_area_circulo(radio):
    area = 3.14 * (radio **2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

radio = float(input("ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo de radio {radio} mts. es {area} mts.")
print(f"El perimetro del circulo de radio {radio} mts. es {perimetro} mts.")

#ejecicio 5

def segundos_a_horas(segundos):
    horas = segundos/3600
    return horas

segundos = int(input("ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print(f"La cantidad de {segundos} segundos equivalen a {horas} horas. ")

#ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = i * numero
        print(f"{i} x {numero} : {resultado}")

numero = int(input("ingrese el numero para la multiplicacion: "))

tabla_multiplicar(numero)

#ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "Error: división por cero"
    
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#ejercicio 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)

print(f"Su IMC es: {resultado:.2f}")

#ejercicio 9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)

print(f"La temperatura en Fahrenheit es: {resultado}")

#ejercicio 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(a, b, c)

print(f"El promedio es: {resultado:.2f}")