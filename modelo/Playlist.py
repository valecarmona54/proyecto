from modelo.cancion import Cancion 
class Playlist:
    def __init__(self, nombre_lista: str, parametro_lista_de_canciones: list[Cancion]=[]):
        self.nombre_lista = nombre_lista
        self.lista_de_canciones: list[Cancion] = parametro_lista_de_canciones

    def agregar_cancion(self, cancion: Cancion): #Mira si ya esta en la lista 
        if cancion in self.lista_de_canciones: #TODO: implementar bien la comparacion de la cancion 
            raise Exception (f"La canción {cancion.nombre_cancion}, ya esta en la playlist. ") 
        else: 
            self.lista_de_canciones.append(cancion)

    def eliminar_cancion (self, cancion: Cancion ):
        for cancion in self.lista_de_canciones:
            if cancion.nombre_cancion == cancion:
                self.lista_de_canciones.remove(cancion)
                return True
        else:
            raise Exception (f"La canción {cancion.nombre_cancion}, no esta en la playlist. ") 

 # Revisar logica de como se elimina libro del carrito el caso de estudio tienda libros
