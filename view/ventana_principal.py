import tkinter 

class VentanaPrincipal:
    def __init__(self):
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Spotify")
        self.ventana.mainloop() #Ejecutar 