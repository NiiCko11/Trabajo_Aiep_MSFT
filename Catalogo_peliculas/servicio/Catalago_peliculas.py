import os    #importamos os para manejar archivo (como este caso borrarlo)


class CatalogoPelicula:            # creamos la clase
    ruta_archivo='peliculas.txt'  # definimos el  atributo de la clase llamando la variable que indica el archivo guardala la peliculas




    @classmethod # decorador @classmethod hace que el metodo que reciba como primer parametro cls(clase) en lugar de self
    def agregar_pelicula(cls ,pelicula):
        with open(cls.ruta_archivo,'a', encoding='utf8') as archivo:  #abrimos el archivo pelicula en modo append ('a') significa que si el archivo no existe se crea y si existe y añade la pelicula
            archivo.write(f'{pelicula.nombre}\n')
# al usar with open el archivo se abre y se cierra automaticamente





    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,'r', encoding='utf8') as archivo: # el archivo lo abrimos en modo lectura ('r')
            print('Catalogo de Peliculas'.center(50,'-'))#imprimimos el catalogo
            print(archivo.read()) #lee contenido de nuestra pnatalla




    @classmethod
    def eliminar_pelicula(cls ):
        try:
            os.remove(cls.ruta_archivo) #os.usamos el remove para borrar el archivo pelicula.txt
            print(f'Pelicula  eliminado : {cls.ruta_archivo}.') #si el archivo es eliminado correctamente enviamos mensaje

        except FileNotFoundError:
            print('Pelicula no existe') # y si no lanza una exepcion monstrando el catalogo no existe

