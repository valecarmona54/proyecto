import tkinter

class VentanaCatalogo:
    def __init__(self):
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Cola de reproduccion")
        self.ventana.geometry("400x400")
        self.listboxCatalogo = tkinter.Listbox(self.ventana)  
        self.listboxCatalogo.pack() 
        
    def mostrar(self):
        self.ventana.mainloop()