import random
from modelo.cancion import Cancion
from pygame import mixer

class Reproductor:
    def __init__(self):
        self.cola_de_reproduccion: list[Cancion]=[]

    def agregar_canciones_a_la_cola(self, canciones:list[Cancion]):
        self.cola_de_reproduccion.append(canciones)

    def activar_modo_aleatorio(self):
        random.shuffle(self.cola_de_reproduccion)

    def reproducir_cancion(self, cancion):
        if cancion:
            self.cancion_actual = cancion
            mixer.init()  
            mixer.music.load(cancion.archivo)
            mixer.music.play()
            print("Reproduciendo:", self.cancion_actual.nombre)

    def pausar(self):
        if mixer.music.get_busy():
            if mixer.music.get_pos() > 0:
                mixer.music.pause()
                print("Canción Pausada")
            else:
                mixer.music.unpause()
                print("Canción reanudada")
        else:
            print("No hay canción en reproducción")

    def siguiente_cancion(self):
        if self.lista_:
            # Detener la canción actual si se está reproduciendo
            mixer.music.stop()

            # Obtener una canción aleatoria de la lista activa
            cancion_aleatoria = random.choice(self.lista_activa)

            # Reproducir la canción aleatoria
            mixer.music.load(cancion_aleatoria.archivo)
            mixer.music.play()
            self.cancion_actual = cancion_aleatoria
            print("Canción omitida")
            print(self.cancion_actual.nombre)




