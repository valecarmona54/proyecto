import tkinter 

class VentanaDePlaylist:
    def __init__(self):
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Playlist")
        self.ventana.geometry("400x400")
        self.BotonVerPlaylist=tkinter.Button(self.ventana, text="Ver lista")
        self.BotonVerPlaylist.pack()
        self.BotonAgregarPlaylist =tkinter.Button(self.ventana, text="Crear lista")
        self.BotonAgregarPlaylist.pack()
        self.listboxCancionesDePlaylist = tkinter.Listbox()
        self.listboxCancionesDePlaylist.pack() 

    def mostrar(self):
        self.ventana.mainloop()
