#Ejercicio 1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

numero = int(input("ingrese un numero: "))

print("\nFactoriales: ")

for i in range(1 , numero + 1):
    print(f"{i}! = {factorial(i)}")

#Ejercicio 2

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
posicion = int(input("Ingrese la posicion maxima: "))

print("\nFibonacci: ")

for i in range(posicion + 1):
    print(f"en la posicion {i} obtenemos el valor de fibonacci: {fibonacci(i)}")


#Ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese un exponente: "))

resultado = potencia(base, exponente)

print(f"\nResultado: {resultado}")


#Ejercicio 4
def decimal_binario(num):
    if num < 2:
        return str(num)
    else:
        return decimal_binario(num // 2) + str(num % 2)

numero = int(input("Ingrese un numero decimal: "))

print(f"El numero {numero} en Binario: {decimal_binario(numero)}")


#Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()

if es_palindromo(texto):
    print("Es palidromo")
else:
    print("No es palidromo")


#Ejercicio 6

def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)

numero = int(input("Ingrese un numero: "))

print(f"la suma de todos los digitos del numero {numero} es: {suma_digitos(numero)} ")

#Ejercicio 7

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)
    
niveles = int(input("Bloques de la base: "))

print(f"Total de bloques: {contar_bloques(niveles)} ")

#Ejercicio 8

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0

    ultimo = numero % 10

    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese un digito: "))

print(f"Cantidad de apariciones: {contar_digito(numero, digito)}")