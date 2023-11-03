import tkinter 
from view.ventana_creacion_playlist import VentanaCreacionPlaylist


class VentanaDePlaylist:
    def __init__(self, ventana_principal):
        self.ventana_principal =ventana_principal
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Playlist")
        self.ventana.geometry("400x400")
        self.BotonVerPlaylist=tkinter.Button(self.ventana, text="Ver lista")
        self.BotonVerPlaylist.pack()
        self.BotonAgregarPlaylist =tkinter.Button(self.ventana, text="Crear lista", command=self.abrir_ventana_creacion_playlist)
        self.BotonAgregarPlaylist.pack()
        self.listboxCancionesDePlaylist = tkinter.Listbox(self.ventana)
        self.listboxCancionesDePlaylist.pack() 


    def abrir_ventana_creacion_playlist(self):
        ventanaCreacionPlaylist = VentanaCreacionPlaylist(self)
        ventanaCreacionPlaylist.mostrar()


    def mostrar(self):
        self.ventana.mainloop()
