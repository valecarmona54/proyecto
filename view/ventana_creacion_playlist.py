import tkinter 

class VentanaCreacionPlaylist:
    def __init__(self, ventanaDePlaylist):
        self.ventanaDePlaylist = ventanaDePlaylist
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Playlist")
        self.ventana.geometry("400x400")
        self.lblNombre =tkinter.Label(self.ventana, text="Nombre")
        self.lblNombre.pack() #Parentesis
        self.txtNombreNuevaPlaylist = tkinter.Entry(self.ventana ,width=10)
        self.txtNombreNuevaPlaylist.insert(0, "Python")
        self.txtNombreNuevaPlaylist.pack()
        self.btnCrearPlaylist =tkinter.Button(self.ventana, text="Crear playlist")
        self.btnCrearPlaylist.pack()
         
    def mostrar(self):
        self.ventana.mainloop()