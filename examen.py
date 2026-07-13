# Datos
'''
"titulo"	    Nombre de la película	No debe contener solo espacios en blanco ni estar vacío
"genero"    	Género cinematográfico	No debe contener solo espacios en blanco ni estar vacío
"duracion_min"	Duración en minutos	Número entero mayor que cero
"clasificacion" Clasificación de audiencia	Debe ser exactamente 'A', 'B' o 'C'
"idioma"	    Idioma original de la película	No debe contener solo espacios en blanco ni estar vacío
"es_3d"	        Indica si la función es en formato 3D	El usuario ingresa 's' o 'n'. El sistema lo convierte a True o False
'''
peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    'P107': ['Avengers End Game', 'acción', 300, 'A', 'Español', True],
    'P108': ['Ms Marvel', 'acción', 120, 'C', 'Español', False],
}

'''
"precio"    	Precio de la entrada en pesos	Número entero mayor que cero
"cupos"     	Cantidad de cupos disponibles para esa función	Número entero mayor o igual a cero
'''
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
    'P107': [10000, 27],
    'P108': [2000, 49],
}
# Fin Datos

# Funciones adicionales
def verficicartexto(texto):
    if texto == "" or texto == " ":
        print("La opcion ingresada debe contener caracteres. ")
        return False
    return True
# Fin funciones adicionales


# Opciones
def cupos_genero(genero):
    total_cupos_disponibles_de_peliculas_por_genero = 0
    for id, pelicula in peliculas.items():
        if pelicula[1] == genero:
            # print(id) # print id de la pelicula correspondiente al genero
            total_cupos_disponibles_de_peliculas_por_genero += int(cartelera[id][1])
    print(f"Hay disponibles {total_cupos_disponibles_de_peliculas_por_genero} cupos para peliculas con el genero {genero}")

def busqueda_precio(p_min, p_max):
    listapeliculas=[]
    for id, preciocupos in cartelera.items():
        if p_min <= preciocupos[0] <= p_max:
            if preciocupos[1] !=0:
                listapeliculas.append(peliculas[id])
    listapeliculas.sort()
    if len(listapeliculas) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print(listapeliculas)

def actualizar_precio(codigo, nuevo_precio):
    for id, preciocupos in cartelera.items():
        if id.lower() == codigo:
            # print(preciocupos[0])
            preciocupos[0] = nuevo_precio
            # print(preciocupos[0])
            print("Precio actualizado")
            return True
    return False

# Utilidades de crear
'''
código          No vacío ni solo espacios en blanco, y que no exista ya en los diccionarios
título	        No vacío ni solo espacios en blanco
género	        No vacío ni solo espacios en blanco
duración	    Número entero mayor que cero
clasificación	Debe ser exactamente 'A', 'B' o 'C'
idioma  	    No vacío ni solo espacios en blanco
es_3d   	    El usuario ingresa 's' o 'n'. El sistema almacena True si es 's', False si es 'n'
precio  	    Número entero mayor que cero
cupos       	Número entero mayor o igual a cero
'''
def rev_codigo(rev1):
    return True
def rev_titulo(rev2):
    return True
def rev_genero(rev3):
    return True
def rev_duracion(rev4):
    return True
def rev_clasificacion(rev5):
    return True
def rev_idioma(rev6):
    return True
def rev_es_3d(rev7):
    return True
def rev_precio(rev8):
    return True
def rev_cupos(rev9):
    return True
# Fin Utilidades de crear

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    for id, precioscupo in cartelera.items():
        if id==codigo:
            print("El código ya existe")
            break
    newPeliculas={codigo: [titulo,genero,duracion,clasificacion,idioma,es_3d]}
    
    newCartelera={codigo: [precio,cupos]}

    return True

def eliminar_pelicula(codigo):
    for id, preciocupos in cartelera.items():
        if id == codigo:
            del cartelera[codigo]
            for id, pelicula in peliculas.items():
                if id == codigo:
                    del peliculas[codigo]
                    print("Película eliminada")
                    return True
    # print(cartelera)
    # print(peliculas)
    print("El código no existe")
    return False
# Fin Opciones

# Funcion Principal

def menu():
    while True:
        try:
            print("========== MENÚ PRINCIPAL ==========")
            print("1. Cupos por género")
            print("2. Búsqueda de películas por rango de precio")
            print("3. Actualizar precio de película")
            print("4. Agregar película")
            print("5. Eliminar película")
            print("6. Salir")
            print("=====================================")
            op= int(input("Ingrese la opcion para acceder al menu correspondiente: "))
            match op:
                case 1: #Cupos Por Genero
                    opgenero = input("Ingrese el nombre del género por el cual desea buscar: ")
                    if verficicartexto(opgenero) == False:
                        return
                    cupos_genero(opgenero)
                case 2: # Busqueda de peliculas por rango de precio
                    while True:
                        try:
                            opminPrecio = int(input("Ingrese el valor minimo de la entrada que desea buscar: "))
                            opmaxPrecio = int(input("Ingrese el valor maximo de la entrada que desea buscar: "))
                            if opmaxPrecio < 0 or opminPrecio < 0:
                                print("Debe ingresar valores iguales o superior a 0")
                                break
                            busqueda_precio(opminPrecio,opmaxPrecio)
                            break
                        except:
                            print("Debe ingresar valores enteros")
                case 3: # Actualizar precio de pelicula
                    while True:
                        opactid = input("ingrese el codigo del producto que desea actualizar: ").lower()
                        opactprecio = int(input("ingrese el valor nuevo del producto: "))
                        actualizar_precio(opactid,opactprecio)
                        Continuar=input("¿Desea actualizar otro precio (s/n)?").lower()
                        match Continuar:
                            case "s":
                                continue
                            case "n":
                                break
                            case _:
                                print("Valor incorrecto volviendo al menu principal.")
                                break
                case 4: # Agregar pelicula
                    rev1 = input("Ingresar Codigo: ")
                    if rev_codigo(rev1) == False:
                        print("El código ya existe")
                        break
                    rev2 = input("Ingresar Titulo: ")
                    if rev_titulo(rev2) == False:
                        break
                    rev3 = input("Ingresar Genero: ")
                    if rev_genero(rev3) == False:
                        break
                    rev4 = input("Ingresar Duracion en minutos: ")
                    if rev_duracion(rev4) == False:
                        break
                    rev5 = input("Ingresar clasificacion A/B/C: ")
                    if rev_clasificacion(rev5) == False:
                        break
                    rev6 = input("Ingresar Idioma")
                    if rev_idioma(rev6) == False:
                        break
                    rev77=True
                    rev7 = input("Ingresar si es 3D s/n: ")
                    if rev_es_3d(rev7) == False:
                        break
                    if rev7.lower == "n":
                        rev77 = False
                    rev8 = int(input("Ingresar precio: "))
                    if rev_precio(rev8) == False:
                        break
                    rev9 = int(input("Ingresar cupos disponibles: "))
                    if rev_cupos(rev9) == False:
                        break
                    agregar_pelicula(rev1,rev2,rev3,rev4,rev5,rev6,rev77,rev8,rev9)
                    print("Película agregada")
                case 5: # Eliminar pelicula
                    opelim = input("ingrese el codigo del producto que desea eliminar: ").upper()
                    eliminar_pelicula(opelim)
                case 6: # Salir
                    print("Programa finalizado.")
                    break
                case _:
                    print("Debe seleccionar una opción válida")
        except:
            print("Valor incorrecto volviendo al menu principal.")

# Fin Funcion Principal

# Ejecutar
menu()