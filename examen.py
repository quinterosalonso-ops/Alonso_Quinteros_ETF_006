peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}


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
