from pygame import mixer
import os 
mixer.init()

class Software:
    def init(self, catalogo_canciones):
        self.catalogo_canciones = catalogo_canciones


    def explorar_directorio(self):
        with os.scandir(self.catalogo_canciones) as canciones:
            for entrada in canciones:
                if entrada.is_file():
                    print(f"Nombre del archivo: {entrada.name}")
                elif entrada.is_dir():
                    print(f"Nombre del subdirectorio: {entrada.name}")

catalogo_canciones = "catalogo_canciones"
mi_software = Software(catalogo_canciones)
mi_software.explorar_directorio()

class Cancion:
    def init(self, nombre):
        self.nombre:str = nombre

class ListaReproduccion:
    def init(self, nombre): # agregar y eliminar 
        self.nombre = nombre
        self.lista_canciones:list[Cancion]= []
    def agregar_cancion_lista(self,cancion):
        self.lista_canciones.append(cancion)
    def eliminar_cancion_lista(self,nombre):
        for cancion in self.lista_canciones:
            if cancion.nombre ==nombre:
                self.lista_canciones.remove(cancion)
                return True
        return False
    def mostrar_canciones_lista(self): 
        print (f"Canciones de la lista {self.nombre}: ")
        for i, cancion in enumerate(self.lista_canciones):
            print (f"{i + 1}.{cancion.nombre}")
        

class Reproductor:
    def init(self):
        self.cola_reproduccion=list[Cancion]= []
    def agregar_canciones_a_cola_de_reproduccion(self, lista_de_canciones: list[Cancion]):
        self.cola_reproduccion.append(lista_de_canciones)
    def crear_lista_reproducciones(self):
        nombre_lista =input("Ingrese el nombre de la lista de producciones: ")
        if nombre_lista in self.lista_reproducciones:
            print ("Ya existe una lista con ese nombre")
        else:
            self.lista_reproducciones[nombre_lista] = ListaReproduccion(nombre_lista)
    def mostrar_listas(self):
        print ("Listas de reproducción creadas")
        for lista_nombre in self.lista_reproducciones:
            print (lista_nombre)
    def mostrar_cancion(self): #Reprodcctor 
            for i, cancion in enumerate(self.lista_canciones):
                print (f"{i + 1}.{cancion.nombre}")
    def reproducir_cola(self):
        pass #Todas las canciones en la cola recorrer e invocar metodo reprocu canciones 


    def reproducir_cancion(self, nombre_cancion:str):
        mixer.music.load(nombre_cancion)
        mixer.music.play()
        #Eliminar cancion de la cola

    


class Usuario:

  def _init_(self, nombre, correo):
    self.nombre = nombre
    self.correo = correo
    self.lista_reproduccion = []

  def crear_lista_de_reproduccion(self, nombre_de_la_lista):
    lista_reproduccion = ListaReproduccion(nombre_de_la_lista)
    self.lista_reproduccion.append(lista_reproduccion)

  def agregar_cancion_a_la_lista(self, nombre_lista, cancion):
    for lista in self.lista_reproduccion:
      if lista.nombre == nombre_lista:
        lista.agregar_cancion_lista(cancion)

  def eliminar_cancion_a_la_lista(self, nombre_lista, cancion):
    for lista in self.lista_reproduccion:
      if lista.nombre == nombre_lista:
        lista.eliminar_cancion_lista(cancion)
  
  def mostrar_canciones_de_una_lista(self):

    for lista in self.lista_reproduccion:
    
      print(f"Canciones de la lista: {lista.nombre}")
      lista.mostrar_canciones_lista()

  def mostrar_listas(self):
    print("Listas de reproducción:")
    for lista in self.lista_reproduccion:
      print(lista.nombre)