# EJERCICIO 1 - FACTORIAL

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)



# EJERCICIO 2 - FIBONACCI

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)



# EJERCICIO 3 - POTENCIA

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)



# EJERCICIO 4 - DECIMAL A BINARIO

def decimal_binario(num):
    if num < 2:
        return str(num)
    else:
        return decimal_binario(num // 2) + str(num % 2)



# EJERCICIO 5 - PALÍNDROMO

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False

    return es_palindromo(palabra[1:-1])



# EJERCICIO 6 - SUMA DE DÍGITOS

def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)



# EJERCICIO 7 - CONTAR BLOQUES

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)



# EJERCICIO 8 - CONTAR DÍGITO

def contar_digito(numero, digito):
    if numero == 0:
        return 0

    ultimo = numero % 10

    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)



# PRUEBAS DEL MÓDULO

if __name__ == "__main__":

    print("Pruebas de funciones recursivas\n")

    print("Factorial de 5:", factorial(5))
    print("Fibonacci de 7:", fibonacci(7))
    print("2 elevado a 5:", potencia(2, 5))
    print("10 en binario:", decimal_binario(10))
    print("Neuquen es palíndromo:", es_palindromo("neuquen"))
    print("Suma de dígitos de 1234:", suma_digitos(1234))
    print("Bloques para base 4:", contar_bloques(4))
    print("Cantidad de 2 en 12233421:", contar_digito(12233421, 2))