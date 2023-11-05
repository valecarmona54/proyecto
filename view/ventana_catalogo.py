import tkinter
from view.ventana_cancion_playlist import VentanaCancionPlaylist

class VentanaCatalogo:
    def __init__(self, ventada_cancion_playlist):
        ventada_cancion_playlist=ventada_cancion_playlist
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Catalogo")
        self.ventana.geometry("400x400")
        self.botonAgregarLaCancionSeleccionada=tkinter.Button(self.ventana, text="Agregar canción")
        self.botonAgregarLaCancionSeleccionada.pack()
        self.listboxCatalogo = tkinter.Listbox(self.ventana)  
        self.listboxCatalogo.pack() 
        self.cargar_catalogo_en_listbox()

    def abrir_ventana_cancion_playlist(self):
        ventada_cancion_playlist = VentanaCancionPlaylist(self)
        #self.ventana.destroy()
        ventada_cancion_playlist.mostrar()


    def cargar_catalogo_en_listbox(self):
            for catalogo in self.ventada_cancion_playlist.ventana_de_playlist.ventana_principal.software.catalogo:
                self.listboxCatalogo.insert(tkinter.END, catalogo.nombre_cancion)
        
    def mostrar(self):
        self.ventana.mainloop()