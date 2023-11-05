import tkinter
from view.ventana_reproductor import VentanaReproductor
from modelo.Playlist import Playlist
from view.ventana_catalogo import VentanaCatalogo
from view.ventana_de_playlist import VentanaDePlaylist

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
        self.botonEliminarCancionDeLaPlaylist =tkinter.Button(self.ventana, text=" - ")
        self.botonEliminarCancionDeLaPlaylist.pack()
        self.listboxCancionesDePlaylist = tkinter.Listbox(self.ventana)  
        self.listboxCancionesDePlaylist.pack() 
        self.cargar_catalogo_en_listbox()

    def abrir_ventana_de_playlist(self):
        ventana_de_playlist = VentanaDePlaylist(self)
        #self.ventana.destroy()
        ventana_de_playlist.mostrar()

    def abrir_ventana_reproductor(self):
        ventanaReproductor = VentanaReproductor(self)
        ventanaReproductor.mostrar()
    
    def abrir_ventana_catalogo(self):
        ventanaCatalogo = VentanaCatalogo(self)
        ventanaCatalogo.mostrar()

    def cargar_catalogo_en_listbox(self):
            for catalogo in self.software.catalogo:
                self.listboxCatalogo.insert(tkinter.END, catalogo.nombre_cancion)


    def agregar_cancion_a_la_playlist(self):
        nueva_cancion=Playlist(self.txtNombreNuevaPlaylist.get())
        self.ventana_de_playlist.ventana_principal.software.agregar_cancion_a_la_playlist(nueva_cancion)
        self.ventana_de_playlist.actualizar_lista_de_reproduccion()
        
    def mostrar(self):
        self.ventana.mainloop()