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
    if texto == "" or texto.strip() == "":
        print("La opcion ingresada debe contener caracteres. ")
        return False
    return True
# Fin funciones adicionales


# Opciones
def cupos_genero(genero):
    total_cupos_disponibles_de_peliculas_por_genero = 0
    for id, pelicula in peliculas.items():
        if pelicula[1].lower() == genero.lower():
            # print(id) # print id de la pelicula correspondiente al genero
            total_cupos_disponibles_de_peliculas_por_genero += int(cartelera[id][1])
    print(f"Hay disponibles {total_cupos_disponibles_de_peliculas_por_genero} cupos para peliculas con el genero {genero}")

def busqueda_precio(p_min, p_max):
    listapeliculas=[]
    for id, preciocupos in cartelera.items():
        if p_min <= preciocupos[0] <= p_max:
            if preciocupos[1] !=0:
                listapeliculas.append(f"{peliculas[id][0]}--{id}")
    listapeliculas.sort()
    if len(listapeliculas) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print(listapeliculas)

def actualizar_precio(codigo, nuevo_precio):
    if nuevo_precio <= 0:
        return False
    for id, preciocupos in cartelera.items():
        if id.upper() == codigo.upper():
            # print(preciocupos[0])
            preciocupos[0] = nuevo_precio
            # print(preciocupos[0])
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
    if rev1 == "" or rev1.strip() == "":
        return False
    for id, precioscupo in cartelera.items():
        if id==rev1.upper():
            return False
    return True

def rev_titulo(rev2):
    if rev2 == "" or rev2.strip() == "":
        return False
    return True

def rev_genero(rev3):
    if rev3 == "" or rev3.strip() == "":
        return False
    return True

def rev_duracion(rev4):
    try:
        if int(rev4) <= 0:
            return False
        return True
    except:
        return False
    
def rev_clasificacion(rev5):
    if rev5.upper() == "A" or rev5.upper() == "B" or rev5.upper() == "C":
        return True
    return False

def rev_idioma(rev6):
    if rev6 == "" or rev6.strip() == "":
        return False
    return True

def rev_es_3d(rev7):
    if rev7.lower() == "s" or rev7.lower() == "n":
        return True
    return False

def rev_precio(rev8):
    try:
        if int(rev8) <= 0:
            return False
        return True
    except:
        return False

def rev_cupos(rev9):
    try:
        if int(rev9) < 0:
            return False
        return True
    except:
        return False

# Fin Utilidades de crear

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    for id, precioscupo in cartelera.items():
        if id==codigo.upper():
            print("El código ya existe")
            return False
    peliculas[codigo.upper()]=[titulo,genero,duracion,clasificacion.upper(),idioma,es_3d]
    cartelera[codigo.upper()]=[precio,cupos]
    return True

def eliminar_pelicula(codigo):
    for id, preciocupos in cartelera.items():
        if id == codigo.upper():
            del cartelera[codigo.upper()]
            for id, pelicula in peliculas.items():
                if id == codigo.upper():
                    del peliculas[codigo.upper()]
                    return True
    # print(cartelera)
    # print(peliculas)
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
                        continue
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
                        opactid = input("ingrese el codigo del producto que desea actualizar: ").upper()
                        opactprecio = int(input("ingrese el valor nuevo del producto: "))
                        if actualizar_precio(opactid,opactprecio):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
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
                    while True:
                        rev1 = input("Ingresar Codigo: ")
                        if rev_codigo(rev1) == False:
                            print("El código ya existe")
                            break
                        
                        rev2 = input("Ingresar Titulo: ")
                        if rev_titulo(rev2) == False:
                            print("La opcion ingresada debe contener caracteres. ")
                            break
                        
                        rev3 = input("Ingresar Genero: ")
                        if rev_genero(rev3) == False:
                            print("La opcion ingresada debe contener caracteres. ")
                            break
                        
                        rev4 = int(input("Ingresar Duracion en minutos: "))
                        if rev_duracion(rev4) == False:
                            print("Debe ingresar un numero entero positivo distinto de 0")
                            break
                        
                        rev5 = input("Ingresar clasificacion A/B/C: ")
                        if rev_clasificacion(rev5) == False:
                            print("Debe ingresar A, B o C como clasificacion")
                            break
                        
                        rev6 = input("Ingresar Idioma: ")
                        if rev_idioma(rev6) == False:
                            print("La opcion ingresada debe contener caracteres. ")
                            break
                        
                        rev7TF=True
                        rev7 = input("Ingresar si es 3D s/n: ")
                        if rev_es_3d(rev7) == False:
                            break
                        if rev7.lower() == "n":
                            rev7TF = False
                        
                        rev8 = int(input("Ingresar precio: "))
                        if rev_precio(rev8) == False:
                            print("Debe ingresar un numero entero positivo distinto de 0")
                            break
                        
                        rev9 = int(input("Ingresar cupos disponibles: "))
                        if rev_cupos(rev9) == False:
                            print("Debe ingresar un numero entero positivo")
                            break
                        agregar_pelicula(rev1,rev2,rev3,rev4,rev5,rev6,rev7TF,rev8,rev9)
                        print("Película agregada")
                        break
                case 5: # Eliminar pelicula
                    opelim = input("ingrese el codigo del producto que desea eliminar: ").upper()
                    if eliminar_pelicula(opelim):
                        print("Película eliminada")
                    else:
                        print("El código no existe")
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