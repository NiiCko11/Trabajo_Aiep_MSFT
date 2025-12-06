from dominio.pelicula import Pelicula
from servicio.Catalago_peliculas import CatalogoPelicula as cp
opcion = None
while opcion != 4:
    try:
        print('''
    ---------------------
       ( BIENVENIDO ) 
    ------ Menu----------
    1.- Agregar Pelicula
            
    2.- Eliminar pelicula
            
    3.- Mostra listado de pelicula
            
    4.- Salir 
    ---------------------''')
        opcion = int(input('Ingresa una opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('ingrese el nombre de la pelicula que desea agregar')
            pelicula=Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
            print('Pelicula agregada exito')

        elif opcion == 2:
            cp.eliminar_pelicula()
            print('Pelicula eliminada exito')

        elif opcion == 3:
            cp.listar_peliculas()

    except ValueError:
        print('Ocurrio un error ')
        opcion=None
        continue


else:
        print('Adios un Gusto ')

