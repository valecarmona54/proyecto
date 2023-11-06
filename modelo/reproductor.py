import random
from modelo.cancion import Cancion
from pygame import mixer

class Reproductor:
    def __init__(self):
        self.cola_de_reproduccion: list[Cancion]=[]
        self.cancion_actual = None

    def agregar_canciones_a_la_cola(self, canciones:list[Cancion]):
        self.cola_de_reproduccion.append(canciones)

    def activar_modo_aleatorio(self):
        random.shuffle(self.cola_de_reproduccion)

    def reproducir_cancion(self, cancion: Cancion):
        if cancion:
            if self.cancion_actual and mixer.music.get_busy():
                print("Deteniendo la canción anterior...")
                mixer.music.stop()
        self.cancion_actual = cancion
        mixer.init()
        mixer.music.load(cancion.direccion_archivo)
        mixer.music.play()
        print("Reproduciendo:", self.cancion_actual.nombre_cancion)
        while mixer.music.get_busy():
            pass
        print("Reproducción finalizada:", self.cancion_actual.nombre_cancion)

"""
    def reproducir_cancion(self, cancion: Cancion):
        if cancion:
            if self.cancion_actual and mixer.music.get_busy():
                print("Deteniendo la canción anterior...")
                mixer.music.stop()
        self.cancion_actual = cancion
        mixer.init()
        mixer.music.load(cancion.direccion_archivo)
        mixer.music.play()
        print("Reproduciendo:", self.cancion_actual.nombre_cancion)
        while mixer.music.get_busy():
            pass
        print("Reproducción finalizada:", self.cancion_actual.nombre_cancion)

"""




