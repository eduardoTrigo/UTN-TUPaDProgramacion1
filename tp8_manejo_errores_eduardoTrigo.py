#Ejercicio 1
a =10
b = input("Introduce un numero: ")

result= a / b # Error: TypeError. input() devuelve un string y no se puede dividir un entero por un string.

print(f"Resultado: {result}")

numbers = [1, 2, 3]

print(numbers[5]) # Error: IndexError. La lista solo tiene posiciones 0, 1 y 2. La posición 5 no existe.

#Ejercicio 2

a = 10
b = input("Ingrese un numero: ")

b = int(b)

if b != 0:
    result = a / b
    print(f"Resultado: {result}")
else:
    print("No se puede dividir por cero.")

numbers = [1, 2, 3]

print(numbers[2])

#Ejercicio 3

try:
    a=10
    b=input("Introduce un numero: ")

    result = a / b
    print(f"Resultado: {result}")

except:
    print("Ocurrio un error en la division.")

try:
    numbers = [1, 2, 3]

    print(numbers[5])

except:
    print("Ocurrio un error al acceder a la lista")

#Ejercicio 4

try:
    a=10
    b=input("Introduce un numero: ")

    result = a / b
    print(f"Resultado: {result}")

except TypeError:
    print("Error: no se puede dividir un numero entero por un texto.")

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")


try:
    numbers = [1, 2, 3]
    print(numbers[5])

except IndexError:
    print("Error: la posicion indicada no existe en la lista")


#Ejercicio 5

try:
    a = 10
    b = input("Introduce un número: ")

    result = a / b
    print(f"Resultado: {result}")

except TypeError:
    print("Error: no se puede dividir un número por un texto.")

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

else:
    print("La división se realizó correctamente.")

finally:
    print("Finalizó el bloque de división.")


try:
    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:
    print("Error: índice fuera de rango.")

else:
    print("Se accedió correctamente a la lista.")

finally:
    print("Finalizó el bloque de lista.")

#Ejercicio 6

try:
    numero = int(input("Ingrese un número: "))

except ValueError:
    print("Debe ingresar un número válido")

except Exception as error:
    print(f"Se produjo un error inesperado:{error}")

else:
    print(f"Número ingresado:{numero}")

#Ejercicio 7

while True:
    try:
        numero = int(input("ingrese un numero: "))

    except ValueError:
        print("Debe ingresar un numero valido.")

    except Exception as error:
        print(f"Se produjo un error inesperado: {error}")
    
    else:
        print(f"Numero ingresado: {numero}")
        break
    
    finally:
        print("Intento finalizado.")
    
