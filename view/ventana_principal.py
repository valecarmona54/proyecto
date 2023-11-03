import tkinter 

class VentanaPrincipal:
    def __init__(self):
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Spotify")
        self.ventana.geometry("400x400")
        self.botonVerPlaylist =tkinter.Button(self.ventana, text="Ver listas")
        self.botonVerPlaylist.pack()
        self.listboxCatalogo = tkinter.Listbox()
        self.listboxCatalogo.pack()
        
    def mostrar(self):
        self.ventana.mainloop()