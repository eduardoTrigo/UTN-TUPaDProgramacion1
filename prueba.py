# import os

# def listar_archivos(directorio,lista):
#     for elemento in os.listdir(directorio):
#         ruta = os.path.join(directorio, elemento)
#         if os.path.isdir(ruta):
#             print(f"Directorio padre {ruta}")
#             print("------------------------------------")
#             listar_archivos(ruta, lista)
#         else:
#             lista_rutas.append(ruta)
#             print(ruta)

# lista_rutas=[]
# listar_archivos(r"L:\sorteos", lista_rutas)
# print(lista_rutas)


##### Fibonachi

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

print(fibonacci_recursivo(7))

if __name__=="__main__":
    print(fibonacci_recursivo(6))


### numero primo

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True