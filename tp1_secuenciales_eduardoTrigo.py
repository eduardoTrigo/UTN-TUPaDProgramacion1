#Alumno : Trigo Estrada Hector Eduardo

#ejercicio 1
print("Hola Mundo!")

#ejercicio 2
nombre = input("ingrese un nombre:\n")
print(f"Hola {nombre}")

#ejercicio 3
nombre = input("ingrese el nombre:\n")
apellido = input("ingrese el apellido:\n")
edad = int(input("ingrese su edad\n"))
residencia = input("ingrese lugar de residencia\n")

print(f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {residencia}")

#ejercicio 4
radio = float(input("ingrese el radio de la circunferencia.\n"))
area =  3.14  * (radio ** 2)
perimetro = 2 * 3.14 * radio

print(f"el area del circulo de radio {radio} es {area} y el perimetro {perimetro}.")

#ejercicio 5
segundos = float(input("ingrese una cantidad de segundos:\n"))
horas = segundos / 60

print(f"{segundos} segundos equivalen a {horas} horas")

#ejercicio 6
numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#ejercicio 7
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc}")

#ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit}")

#ejercicio 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es: {promedio}")
