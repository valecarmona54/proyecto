import tkinter

class VentanaCancionPlaylist:
    def __init__(self):
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Canciones de una playlist")
        self.ventana.geometry("400x400")
        self.botonReproducirPlaylist =tkinter.Button(self.ventana, text=" Reproducir ")
        self.botonReproducirPlaylist.pack()
        self.lblAgregarCancionPlaylist =tkinter.Label(self.ventana, text="Agregar canción a la playlist")
        self.lblAgregarCancionPlaylist.pack() 
        self.botonAgregarCancionALaPlaylist =tkinter.Button(self.ventana, text=" + ")
        self.botonAgregarCancionALaPlaylist.pack()
        self.lblEliminarCancionDeLaPlaylist =tkinter.Label(self.ventana, text="Eliminar Cancion de la Playlist")
        self.lblEliminarCancionDeLaPlaylist.pack() 
        self.botonEliminarCancionDeLaPlaylist =tkinter.Button(self.ventana, text=" - ")
        self.botonEliminarCancionDeLaPlaylist.pack()
        self.listboxCancionesDePlaylist = tkinter.Listbox(self.ventana)  
        self.listboxCancionesDePlaylist.pack() 
        
    def mostrar(self):
        self.ventana.mainloop()