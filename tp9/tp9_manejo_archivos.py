# 4) cargar productos

productos = []

# 2)Leer y Mostrar productos
with open("productos.txt", "r" , encoding="utf-8") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")

        producto = {
            "nombre" : partes[0],
            "precio" : float(partes[1]),
            "cantidad" : int(partes[2])
        }

        productos.append(producto)



print("\nLISTA DE PRODUCTOS")

for producto in productos:

    print(
        f"Producto: {producto['nombre']} | "
        f"Precio: ${producto['precio']} | "
        f"Cantidad: {producto['cantidad']}"
    )

# 3) AGREGAR NUEVO PRODUCTO

print("\nAGREGAR NUEVO PRODUCTO")

nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

nuevo_producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}

productos.append(nuevo_producto)

with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(
        f"\n{nombre},{precio},{cantidad}"
    )

print("Producto agregado correctamente")

#5) Buscar Producto

buscar = input("\nIngrese producto a buscar: ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscar.lower():
        print("\nPRODUCTO ENCONTRADO")

        print("Nombre: ", producto["nombre"])
        print("Precio: ", producto["precio"])
        print("Cantidad", producto["cantidad"])

        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

#6) Guardar nuevamente todos los productos 

with open("productos.txt", "w" , encoding="utf-8") as archivo:
    for producto in productos:
        linea = (
            f"{producto['nombre']}"
            f"{producto['precio']}"
            f"{producto['cantidad']}\n"
        )
        archivo.write(linea)

print("\nArchivo actualizado correctamente.")