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
    'P106': [7490, 3]
}
# Fin Datos

# Opciones
def cupos_genero(genero):
    pass

def busqueda_precio(p_min, p_max):
    print()

def actualizar_precio(codigo, nuevo_precio):
    return True

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
def rev_codigo():
    pass
def rev_titulo():
    pass
def rev_genero():
    pass
def rev_duracion():
    pass
def rev_clasificacion():
    pass
def rev_idioma():
    pass
def rev_es_3d():
    pass
def rev_precio():
    pass
def rev_cupos():
    pass
# Fin Utilidades de crear

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    return True

def eliminar_pelicula(codigo):
    return True
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
            op= int(input("Ingrese la opcion para acceder al menu correspondiente"))
            match op:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case _:
                    pass
        except:
            pass
# Fin Funcion Principal

# Ejecutar
menu()