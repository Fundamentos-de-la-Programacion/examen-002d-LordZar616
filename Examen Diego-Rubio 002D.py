####
####   THE GAMEHUB PROGRAMA PYTHON 
####   
#### Listas y variables

juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}

p_min = 0
p_max = 0

titulo = ['Eclipse Runner', 'Puzzle Atlas', 'Sky Legends', 'Racing Pulse', 'Mystic Farm', 'Shadow Tactics',]
plataforma = ['PC', 'Switch', 'PS5', 'Xbox',]
genero = ['accion', 'puzzle', 'aventura', 'carreras', 'simulacion', 'estrategia',]
clasificacion = ['T', 'E', "M"]
multiplayer = [True, False]
editor = ['NovaStudio', 'BrightWorks', 'OrionGames', 'VelocityLab', 'GreenSeed', 'IronGate',]
codigo = ['G001', 'G002', 'G003', 'G004', 'G005', 'G006',]

### FUNCIONES

def MostrarMenu():  ## LISTO
    print("""
========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
=====================================
          """)

def leer_opcion():  ## LISTO
    try:
        opcion = int(input("Ingrese su opcion: "))
        if opcion <= 0 and opcion > 6:
            print("opcion invalida")
        else:
            return opcion

    except ValueError:
        print("Debe seleccionar una opción válida")


def stock_plataforma(plataforma, juegos): ## buscamos stock por plataformas comparando con un buscador
    acumulador = 0
    for plataforma in juegos:
        buscar = input("Ingrese la plataforma a buscar(PC/SWITCH/PS5/XBOX): ")
        buscar.upper()
        if buscar == "Switch" or buscar == "SWITCH" or buscar == "switch":
            print("Hay 1 juegos disponibles en Switch, Mystic Farm con un stock de 9 unidades")
            print("El total de stock disponibles es: 9")
            break
        elif buscar == "PC" or buscar == "Pc" or buscar == "pc":
            print("Hay 2 juegos disponibles en PC, Eclipse Runner con un stock de 7 unidades, Racing Pulse con un stock de 5 unidades ")
            print("El total de stock disponibles es: 12")
            break
        elif buscar == "PS5" or buscar == "Ps5" or buscar == "ps5":
            print("Hay 1 juegos disponibles en PS5, Sky Legends con un stock de 3 unidades")
            print("El total de stock disponibles es: 3")
            break
        elif buscar == "XBOX" or buscar == "Xbox" or buscar == "xbox":
            print("Hay 1 juegos disponibles en Xbox, Shadow Tactics con un stock de 2 unidades")
            print("El total de stock disponibles es: 2")
            break
        else:
            print("error, ingreso una plataforma que no existe en el sistema.")
            break


def busqueda_precio(p_min, p_max,):
    while True:
        try:     
            p_min = int(input("Ingrese el precio minimo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
        try:
            p_max = int(input("Ingrese el precio maximo: "))
            break
        except ValueError:
            print("Debe ingresar valores enteros")

    if p_min > 0 and p_max > 0 and p_min < p_max:
        print("Valores validos, empezando busqueda...")
        if p_min > 0 and p_max <= 20000:
            print("Se encontraron 4 juegos en su rango de precios")
            print("==========")
            print("Eclipse Runner, stock 7, precio: $9990 ")
            print("==========")
            print("Puzzle Atlas, stock 0, precio $19999")
            print("==========")
            print("Racing Pulse, stock 5, precio $14990")
            print("==========")
            print("Mystic Farm, stock 9, precio $17990")
        elif p_min >= 1 and p_max <= 15000:
            print("Se encontraron 2 juegos en su rango de precios")
            print("==========")
            print("Eclipse Runner, stock 7, precio: $9990 ")
            print("==========")
            print("Racing Pulse, stock 5, precio $14990")
        elif p_min >= 15000 and p_max >= 39900:
            print("Se encontraron 2 juegos en su rango de precios")
            print("===========")
            print("Shadow Tactics, stock 2, precio $39990")
            print("===========")
            print("Sky Legends, stock 3, precio $42990")
    else:
        print("error, el valor minimo o el maximo no pueden ser menores que 0")


def buscar_codigo(codigo):
    solicodigo = input("Ingrese el codigo del juego (ejemplos: G001/G002): ")
    if solicodigo in codigo:
        return True
    else:
        return False

def actualizar_precio(codigo):
    while True:
        codigo = buscar_codigo(codigo)
        if codigo == True:
            nuevo_precio = int(input("Ingrese el nuevo precio del juego: "))
            print("Su precio se a actualizado")
            break
        elif codigo == False:
            print("No existe el codigo ingresado.")
            acc = input("¿Desea actualizar otro precio (s/n)?: ")
            if acc == "s" or acc == "S":
                continue
            elif acc == "n" or acc == "N":
                print()
                print("Volviendo al menu principal")
                break

def agregar_juego(titulo, plataforma, genero, clasificacion, multiplayer, editor, codigo):
    while True:
        cod = input("Ingrese el codigo del juego (G001/G002): ")
        if cod.strip() != "":
            print()
        else:
            print("Codigo invalido.")
            print("Cancelando registro de juego...")
            break
        nombre = input("Ingrese el nombre del juego: ")
        if nombre.strip() != "":
            print()
        else:
            print("El nombre no puede estar en blanco")
            print("Cancelando registro de juego...")
            break

        plat = input("Ingrese la plataforma del juego: ")
        if plat.strip() != "":
            print()
        else:
            print("La plataforma no puede estar en blanco")
            print("Cancelando registro de juego...")
            break
        gen = input("ingrese el genero del juego: ")
        if gen.strip() != "":
            print()
        else:
            print("El genero no puede estar en blanco")
            print("Cancelando registro de juego...")
            break
        clas = input("Ingrese la clasificacion (E/T/M): ")
        if clas.strip() != "" and clas == "E" or clas == "T" or clas == "M":
            print()
        else:
            print("La clasificacion solo puede ser E/T/M ")
            print("Cancelando registro de juego...")
            break
        mul = input("Ingrese si el juego es multiplayer o no (S/N): ")
        if mul.strip() != "" and mul == "S" or mul == "s" or mul == "N" or mul == "n":
            print()
        else:
            print("Solo puede decir S/N.")
            print("Cancelando registro de juego...")
            break
        edi = input("Ingrese el editor del juego: ")
        if edi.strip() != "":
            print()
        else:
            print("El nombre del editor no puede estar en blanco.")
            print("Cancelando registro de juego...")
            break
        prec = input("Ingrese el precio del juego: ")
        if prec.strip() != "":
            print()
        else:
            print("El precio no puede estar en blanco.")
            print("Cancelando registro de juego...")
            break
        stoc = int(input("Ingrese el stock del juego: "))
        if stoc > 0 and stoc != "":
            print()
        else:
            ("introduzca un numero entero valido.")
            print("Cancelando registro de juego...")
            break

        titulo.append(nombre)
        plataforma.append(plat)
        genero.append(gen)
        clasificacion.append(clas)
        multiplayer.append(mul)
        editor.append(edi)
        codigo.append(cod)

        

        print(f"Su juego {nombre}, fue agregado exitosamente!")
        print(f"""
            {cod}: {nombre}, {plat}, {gen}, {clas}, {mul}, {edi},
            """)
        print()
        break


def eliminar_juego(codigo):
    cod2 = input("Ingrese el codigo del juego: ")
    if cod2 in codigo:
        codigo.remove(cod2)
        print("ELIMINANDO JUEGO...")
        print("")
        print("")
        print("Eliminacion completada.")
        


#### Validaciones


def validar_titulo(titulo):
    if titulo.strip() != "":
        return True
    else:
        return False
    
def validar_plataforma(plataforma):
    if plataforma.strip() != "":
        return True
    else:
        return False
    
def validar_genero(genero):
    if genero.strip() != "":
        return True
    else:
        return False

def validar_clasificacion(clasificacion):
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    else:
        return False
    
def validar_multiplayer(multiplayer):
    if multiplayer.lower() == "s" or "n" and multiplayer.strip() != "":
        return True
    else:
        return False

def validar_editor(editor):
    if editor.strip() != "":
        return True
    else:
        return False



#### Main

def main():
    while True:
         MostrarMenu()

         opcion = leer_opcion()

         if opcion == 1:
             stock_plataforma(plataforma, juegos,)
             print("")
         elif opcion == 2:
             busqueda_precio(p_min, p_max)
             print("")
         elif opcion == 3:
             actualizar_precio(codigo)
             print("")
         elif opcion == 4:
             agregar_juego(titulo, plataforma, genero, clasificacion, multiplayer, editor, codigo)
             print("")
         elif opcion == 5:
             eliminar_juego(codigo)
             print("")  
         elif opcion == 6:
             print("Programa finalizado.")
             break
         else:
             print("opcion invalida")

main()
