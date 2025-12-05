

class Pelicula:

    def __init__(self,nombre):  # creamos el atributo
        self.nombre=nombre    #contructor

    def __str__(self):        #metodos para mostrar pelicula
        return f'Pelicula: {self.nombre}'



    @property
    # decorador en python que se utiliza para converti
    # en solo lectura en un atrbibuto en otras palabra en definir un getter sin necesidad de llamar a la funcion
    def nombre(self):
        return self._nombre

#usamor setter para modificar el valor del atributo privado
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre =nuevo_nombre