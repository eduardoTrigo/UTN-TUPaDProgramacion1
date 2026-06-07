from funciones_recursivas import *



# EJERCICIO 1

numero = int(input("Ingrese un número: "))

print("\nFactoriales:")

for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")



# EJERCICIO 2

posicion = int(input("\nIngrese la posición máxima: "))

print("\nSerie Fibonacci:")

for i in range(posicion + 1):
    print(f"Posición {i}: {fibonacci(i)}")



# EJERCICIO 3

base = int(input("\nIngrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"Resultado: {potencia(base, exponente)}")



# EJERCICIO 4

numero = int(input("\nIngrese un número decimal: "))

print(
    f"El número {numero} en binario es: "
    f"{decimal_binario(numero)}"
)



# EJERCICIO 5

palabra = input("\nIngrese una palabra: ").lower()

if es_palindromo(palabra):
    print("Es palíndromo")
else:
    print("No es palíndromo")



# EJERCICIO 6

numero = int(input("\nIngrese un número: "))

print(
    f"La suma de los dígitos del número "
    f"{numero} es: {suma_digitos(numero)}"
)



# EJERCICIO 7

niveles = int(input("\nBloques de la base: "))

print(
    f"Total de bloques: "
    f"{contar_bloques(niveles)}"
)



# EJERCICIO 8

numero = int(input("\nIngrese un número: "))
digito = int(input("Ingrese un dígito: "))

print(
    f"Cantidad de apariciones: "
    f"{contar_digito(numero, digito)}"
)