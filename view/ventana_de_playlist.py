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
        self.listboxDePlaylist = tkinter.Listbox(self.ventana, command=self.actualizar_lista_de_playlist)  #Revisar
        self.listboxDePlaylist.pack() 


    def abrir_ventana_creacion_playlist(self):
        ventanaCreacionPlaylist = VentanaCreacionPlaylist(self)
        ventanaCreacionPlaylist.mostrar()

    def actualizar_lista_de_playlist(self):
        self.listboxDePlaylist.delete(0, tkinter.END)
        for playlist in self.listboxDePlaylist:
            self.listboxDePlaylist.insert(tkinter.END, playlist) 
        



    def mostrar(self):
        self.ventana.mainloop()
