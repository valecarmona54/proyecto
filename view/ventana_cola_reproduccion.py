import tkinter

class VentanaColaReproduccion:
    def __init__(self):
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Catalogo")
        self.ventana.geometry("400x400")
        self.listboxColaDeReproduccion = tkinter.Listbox(self.ventana)  
        self.listboxColaDeReproduccion.pack() 
        
    def mostrar(self):
        self.ventana.mainloop()