#Trigo Estrada Hector Eduardo

#ejercicio1
nombre = input("ingrese un nombre: ")
while not nombre.isalpha() or nombre == "" :
    nombre = input("ingrese nuevamente un nombre: ")

cantidad = input("ingrese una cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("ingrese un numero entero positivo: ")
cantidad = int(cantidad)

desc_total = 0
total = 0

print(f"cliente : {nombre}")
print(f"cantidad de productos: {cantidad}")

for i in range(1, cantidad+1):
    precio = input(f"ingrese el precio del producto {i}: ")
    while not precio.isdigit() or int(precio) <=0:
        precio = input(f"ingrese nuevamente el precio del producto {i}: ")
    precio = int(precio)

    desc = input("este producto tiene descuento? S/N : ").lower()
    while desc != "s" and desc != "n":
        desc = input("Ingrese S o N: ").lower()
    if desc == "s" or desc == "S":
        monto_desc = float(precio) * 0.1
    else:
        monto_desc = 0

    total += precio 
    desc_total += monto_desc

    print(f"Producto {i} - Precio : ${precio} - Descuento (S/N): {desc. upper()}")

total_pagar = float(total - desc_total)
promedio = total_pagar / cantidad

print("\n")
print(f"Total sin descuento: ${total}")
print(f"total con descuento: ${total_pagar:.2f}")
print(f"Ahorro: ${desc_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")



#ejercicio 2
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:
    print(f"intento{intentos+1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido. ")
    else:
        print("Error: Credenciales Invalidas")
        intentos += 1
        if intentos == 3:
            print("Cuenta bloqueada.")
    
while acceso :
    opcion = input("Elija una Opcion:\n" \
                   "1)Estado de Inscripcion\n" \
                   "2)Cambiar Clave\n" \
                   "3)Frase motivadora\n" \
                   "4)Salir" \
                   "Opcion:")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
        opcion = input("Error: ingrese una opción válida (1-4): ")
    
    if opcion == "1":
        print("Inscripto.")
    elif opcion == "2":
        clave_nueva = input("Nueva Clave: ")
        while len(clave_nueva )< 6:
            clave_nueva = input("Mínimo 6 caracteres. Nueva clave: ")
        confirmar = input("Confirmar clave: ")
        while clave_nueva != confirmar:
            confirmar = input("Las claves no coinciden. Confirmar Clave: ")

        clave_correcta = clave_nueva
        print("Clave cambiada correctamente.")
    elif opcion == "3":
        print("Seguí adelante, vas mejorando con cada ejercicio.")
    elif opcion == "4":
        acceso = False

print("SALIENDO.....")


#ejercicio 3

operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    operador = input("Ingrese nuevamente el nombre del operador: ")

salir = False

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while not salir:
    opcion = input("Elija una opcion:\n" \
                   "1)Reservar turno.\n" \
                   "2)Cancelar turno (por nombre).\n" \
                   "3)Ver agenda del dia.\n" \
                   "4)Ver resumen general.\n" \
                   "5)Salir")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion = input("ingrese una opcion valida (del 1 al 5): ")
    
    if opcion == "1":
        print("Reservar turno.")

        paciente = input("ingrese nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("ingrese nuevamente el nombre del paciente: ")

        dia = input("ingrese el dia:\n" \
                    "1)Lunes. " \
                    "2)Martes. ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("ingrese nuevamente el dia 1)Lunes o 2)Martes")
        
        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print ("Ya tiene un turno reservado el Lunes.")
            else:
                if lunes1 == "":
                    lunes1 = paciente
                    print("turno reservado para el dia Lunes , Turno 1")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("turno reservado para el dia Lunes , Turno 2")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("turno reservado para el dia Lunes , Turno 3")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("turno reservado para el dia Lunes , Turno 4")
                else:
                    print("No hay cupos disponibles para Lunes.")
        elif dia == "2":
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print ("Ya tiene un turno reservado el Martes.")
            else:
                if martes1 == "":
                    martes1 = paciente
                    print("turno reservado para el dia Martes , Turno 1")
                elif martes2 == "":
                    martes2 = paciente
                    print("turno reservado para el dia Martes , Turno 2")
                elif martes3 == "":
                    martes3 = paciente
                    print("turno reservado para el dia Martes , Turno 3")
                else:
                    print("No hay cupos disponibles para Martes.")

    elif opcion == "2":
        print("Cancelar turno.")

        paciente = input("ingrese nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("ingrese nuevamente el nombre del paciente: ")

        dia = input("ingrese el dia:\n" \
                    "1)Lunes. " \
                    "2)Martes. ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("ingrese nuevamente el dia 1)Lunes o 2)Martes")

        if dia == "1":
            if paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado")
            elif paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado")
            elif paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado")
            elif paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado")
            else:
                print("Ese paciente no tiene turno en Lunes.")
        elif dia == "2":
            if paciente == martes1:
                martes1 = ""
                print("Turno cancelado")
            elif paciente == martes2:
                martes2 = ""
                print("Turno cancelado")
            elif paciente == martes3:
                martes3 = ""
                print("Turno cancelado")
            else:
                print("Ese paciente no tiene turno en martes.")
    elif opcion == "3":
        print("ver agenda del dia")
        dia = input("ingrese el dia:\n" \
                    "1)Lunes. " \
                    "2)Martes. ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("ingrese nuevamente el dia 1)Lunes o 2)Martes")
        
        if dia == "1":
            print("Agenda dia Lunes: ")
            if lunes1 == "":
                print("Turno 1: LIBRE")
            else:
                print(f"Turno 1: {lunes1}")
            
            if lunes2 == "":
                print("Turno 2: LIBRE")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: LIBRE")
            else:
                print(f"Turno 3: {lunes3}")
            
            if lunes4 == "":
                print("Turno 4: LIBRE")
            else:
                print(f"Turno 4: {lunes4}")
        elif dia == "2":
            print("Agenda dia Martes: ")
            if martes1 == "":
                print("Turno 1 : LIBRE")
            else:
                print(f"Turno 1 : {martes1}")
            
            if martes2 == "":
                print("Turno 2 : LIBRE")
            else:
                print(f"Turno 2 : {martes2}")
            
            if martes3 == "":
                print("Turno 3 : LIBRE")
            else:
                print(f"Turno 3 : {martes3}")

    elif opcion == "4":
        print("ver resumen general")
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print(f"Lunes: ocupados {ocupados_lunes} - disponibles {disponibles_lunes}")
        print(f"Martes: ocupados {ocupados_martes} - disponibles {disponibles_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Hay empate entre Lunes y Martes")
    elif opcion == "5":
        print("Salir.")
        salir = True
print("SALIENDO....")

#ejercicio 4 

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

agente = input("ingrese el nombre del agente:")
while not agente.isalpha():
    agente = input("ingrese nuevamente el nombre del agente: ")

bloqueado = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado :
    print("\n" \
         f"Agente: {agente}\n"
         f"Energia: {energia}\n"
         f"Tiempo: {tiempo}\n"
         f"Cerraduras abiertas: {cerraduras_abiertas}\n"
         f"Alarma: {alarma}\n"
         f"Codigo parcial: {codigo_parcial}\n")
    print("\n")
    print("Menu de acciones" \
          "1) Forzar cerradura (-20 energia, -2tiempo)" \
          "2) Hackear panel (-10 energia,-3 tiempo)" \
          "3) Descansar (+15 energia max 100, -1 tiempo)")
    opcion = input("Elija una opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Ingrese una opción válida (1, 2 o 3): ")

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:
            alarma = True
            print("\nLa cerradura se trabo por forzarla tres veces")
            print("Se activa la alarma. No se abre ninguna cerradura")

        else:
            if energia < 40:
                numero = input("Riezgo de alarma. Elija un numero del 1 al 3: ")
                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    numero = input("Ingrese un numero valido del 1 al 3: ")
                
                if numero == "3":
                    alarma = True
                    print("Elegiste 3. ¡la alarma se activo!")
            
            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura. ")
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("\nHackeando panel...")
        for i in range(1,5):
            print(f"Paso {i} completado")
            codigo_parcial += "A"
        
        print(f"Codigo parcial actual: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso! Se abrio una cerradura.")
    
    elif opcion == "3":
        tiempo -= 1
        energia += 15
        if energia > 100:
            energia = 100
        forzar_seguidas = 0

        if alarma:
            energia -= 10
            print("\nDescansaste, pero se activo la alarma (-10 energia)")
        
        print("Descansaste y recuperaste energia.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

print("\n---RESULTADO FINAL---")
print(f"Energia: {energia}")
print(f"Tiempo: {tiempo}")
print(f"cerraduras abiertas: {cerraduras_abiertas}")
print(f"Alarma: {alarma}")
print(f"Codigo parcial: {codigo_parcial}")

if cerraduras_abiertas == 3:
    print("VICTORIA: Lograste abrir la bobeda.")
elif bloqueado :
    print("DERROTA: El sistema se bloqueó por la alarma.")
else:
    print("DERROTA: Te quedaste sin energía o sin tiempo.")
    
    
#ejercicio 5

print("--Bienvenido a la Arena--")

nombre = input("Ingrese el nombre del Gladiador: ")
while not nombre.isalpha():
    nombre = input("Ingrese nuevamente el nombre del Gladiador ( solo se permiten letras): ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("\n INICIO DE COMBATE ")

while vida_jugador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) -- Pociones: {pociones}")
        print("Elige una accion: ")
        print("1) Ataque Pesado")
        print("2) Rafaga Veloz ")
        print("3) Curar ")

        opcion = input("opcion:")
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            opcion = input("Ingrese una opcion valida ( del 1 al 3):")

        if opcion == "1":
            if vida_enemigo < 20:
                danio_turno = danio_pesado *1.5
                vida_enemigo -= danio_turno
                print(f"¡Golpe critico! Atacaste al enemigo por {danio_turno} puntos por daño.")
            else:
                danio_turno = danio_pesado
                vida_enemigo -= danio_turno
                print(f"Atacaste al enemigo por {danio_turno} puntos por daño!")
        elif opcion == "2":
            print("Rafaga de golpes")
            for i in range(3):
                vida_enemigo -= 5
                print("Golpe conectado por 5 de daño")
        elif opcion == "3":
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Recuperaste 30 de vida.")
            else:
                print("No te quedan pociones")

        turno_gladiador = False

    else:
        if vida_enemigo > 0:
            vida_jugador -= danio_enemigo
            print(f"El enemigo te ataco por {danio_enemigo} puntos de daño.")
        
        turno_gladiador = True
        print(" NUEVO TURNO ")

if vida_jugador > 0:
    print(f"\nVICTORIA - {nombre} ha ganado la batalla")
else:
    print("\nDERROTA. Has caido en combate.")
