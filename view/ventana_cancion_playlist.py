import tkinter
from view.ventana_reproductor import VentanaReproductor
from view.ventana_catalogo import VentanaCatalogo
from tkinter import messagebox

class VentanaCancionPlaylist:
    def __init__(self, ventana_de_playlist, playlist):
        self.ventana_de_playlist = ventana_de_playlist
        self.playlist=playlist
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Canciones de una playlist")
        self.ventana.geometry("400x400")
        self.botonReproducirPlaylist =tkinter.Button(self.ventana, text=" Reproducir ", command=self.abrir_ventana_reproductor)
        self.botonReproducirPlaylist.pack()
        self.lblAgregarCancionPlaylist =tkinter.Label(self.ventana, text="Agregar canción a la playlist")
        self.lblAgregarCancionPlaylist.pack() 
        self.botonAgregarCancionALaPlaylist =tkinter.Button(self.ventana, text=" + ", command=self.abrir_ventana_catalogo)
        self.botonAgregarCancionALaPlaylist.pack()
        self.lblEliminarCancionDeLaPlaylist =tkinter.Label(self.ventana, text="Eliminar Cancion de la Playlist")
        self.lblEliminarCancionDeLaPlaylist.pack() 
        self.botonEliminarCancionDeLaPlaylist =tkinter.Button(self.ventana, text=" - ", command=self.eliminar_cancion_de_playlist)
        self.botonEliminarCancionDeLaPlaylist.pack()
        self.listboxCancionesDePlaylist = tkinter.Listbox(self.ventana)  
        self.listboxCancionesDePlaylist.pack() 
        
    def abrir_ventana_reproductor(self):
        ventanaReproductor = VentanaReproductor(self)
        ventanaReproductor.mostrar()
    
    def abrir_ventana_catalogo(self):
        ventanaCatalogo = VentanaCatalogo(self, self.playlist)
        ventanaCatalogo.mostrar()

    def cargar_canciones(self):
        self.listboxCancionesDePlaylist.delete(tkinter.END)
        for cancion in self.playlist.lista_de_canciones:
            self.listboxCancionesDePlaylist.insert(tkinter.END, cancion)

   
    def eliminar_cancion_de_playlist(self):
        indice_item_seleccionado = self.listboxCancionesDePlaylist.curselection()
        if indice_item_seleccionado:
            self.listboxCancionesDePlaylist.delete(indice_item_seleccionado)
            cancion_seleccionada = self.listboxCancionesDePlaylist.get(indice_item_seleccionado[0])
            self.ventana_de_playlist.ventana_principal.software.eliminar_cancion_de_la_playlist(self.playlist, cancion_seleccionada)

                
    def mostrar(self):
        self.ventana.mainloop()