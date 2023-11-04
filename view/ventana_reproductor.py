import tkinter

class VentanaReproductor:
    def __init__(self):
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Reproductor")
        self.ventana.geometry("400x400")
        self.lblPausaDespausa =tkinter.Label(self.ventana, text="Pausa y despausa")
        self.lblPausaDespausa.pack() 
        self.botonPausaDespausa =tkinter.Button(self.ventana, text=" = ")
        self.botonPausaDespausa.pack()
        self.lblCancionAnterios =tkinter.Label(self.ventana, text="Cancion anterior")
        self.lblCancionAnterios.pack() 
        self.botonCancionAnterior =tkinter.Button(self.ventana, text=" < ")
        self.botonCancionAnterior.pack()
        self.lblCancionSiguiente =tkinter.Label(self.ventana, text="Cancion siguiente")
        self.lblCancionSiguiente.pack() 
        self.botonCancionSiguiente =tkinter.Button(self.ventana, text=" > ")
        self.botonCancionSiguiente.pack()
        self.botonColaDeReproduccion =tkinter.Button(self.ventana, text=" Cola de reproducción ")
        self.botonColaDeReproduccion.pack()
        self.botonColaAleatoria =tkinter.Button(self.ventana, text=" Cola aleatoria ")
        self.botonColaAleatoria.pack()
        
    def mostrar(self):
        self.ventana.mainloop()