from modelo.Playlist import Playlist
from modelo.cancion import Cancion
import os
class Software:
    def __init__(self):
        self.listas_de_reproduccion:list[Playlist]=[]
        self.catalogo:list[Cancion]=self._cargar_catalogo()
    
    def _cargar_catalogo(self) -> list[Cancion]:
        lista_canciones: list[Cancion]=[]
        with os.scandir("resources") as carpeta:
            for archivo in carpeta:
                if archivo.is_file():
                    #print(f"Nombre del archivo: {archivo.name}")
                    cancion1=Cancion(archivo.name.replace('_',' '),archivo.name)
                    lista_canciones.append(cancion1)
        return lista_canciones
    
    def agregar_cancion_a_la_playlist(self, playlist: Playlist, nombre_cancion: str ): #Mira si esta en el catalogo y lo agrega a la lista 
        for cancion in self.catalogo:
            if nombre_cancion == cancion.nombre_cancion: #TODO implementar bien la comparacion de la cancion 
                playlist.agregar_cancion(cancion)
                return
        
    def eliminar_cancion_de_la_playlist(self, playlist: Playlist, nombre_cancion:str ):
        for cancion in playlist.lista_de_canciones:
            if  nombre_cancion == cancion.nombre_cancion:
                playlist.eliminar_cancion(cancion)
                return
    
    def agregar_playlist(self, playlist: Playlist):
        if playlist in self.listas_de_reproduccion:
            raise Exception (f"La existe una playlist con ese nombre")
        else:
            self.listas_de_reproduccion.append(playlist)    

