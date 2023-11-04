from modelo.cancion import Cancion
class Reproductor:
    def __init__(self):
        self.cola_de_reproduccion: list[Cancion]=[]

    def agregar_canciones_a_la_cola(self, canciones:list[Cancion]):
        self.cola_de_reproduccion.append(canciones)

    def activar_modo_aleatorio (self):
        #TODO: desordenar cola de reproduccion
        pass