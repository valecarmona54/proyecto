import tkinter 
from modelo.software import Software
from view.ventana_de_playlist import VentanaDePlaylist

class VentanaPrincipal:
    def __init__(self):
        self.software = Software()
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Spotify")
        self.ventana.geometry("400x400")
        self.botonVerPlaylist =tkinter.Button(self.ventana, text="Ver listas",command=self.abrir_ventana_de_playlist)
        self.botonVerPlaylist.pack()
        self.listboxCatalogo = tkinter.Listbox(self.ventana)
        self.listboxCatalogo.pack()

    def abrir_ventana_de_playlist(self):
        ventanaDePlaylist = VentanaDePlaylist(self)
        #self.ventana.destroy()
        ventanaDePlaylist.mostrar()
        

        
    def mostrar(self):
        self.ventana.mainloop()