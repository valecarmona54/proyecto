import tkinter
from tkinter import messagebox
class VentanaCatalogo:
    def __init__(self, ventana_cancion_playlist, playlist):
        self.ventana_cancion_playlist=ventana_cancion_playlist
        self.playlist=playlist
        self.ventana: tkinter.Tk= tkinter.Tk() 
        self.ventana.title("Catalogo")
        self.ventana.geometry("400x400")
        self.botonAgregarLaCancionSeleccionada=tkinter.Button(self.ventana, text="Agregar canción", command=self.agregar_cancion_a_la_playlist)
        self.botonAgregarLaCancionSeleccionada.pack()
        self.listboxCatalogo = tkinter.Listbox(self.ventana)  
        self.listboxCatalogo.pack() 
        self.cargar_catalogo_en_listbox()

    def cargar_catalogo_en_listbox(self):
            for cancion in self.ventana_cancion_playlist.ventana_de_playlist.ventana_principal.software.catalogo:
                self.listboxCatalogo.insert(tkinter.END, cancion)

    def agregar_cancion_a_la_playlist(self):
        indice_item_seleccionada = self.listboxCatalogo.curselection()
        cancion_seleccionada = self.listboxCatalogo.get(indice_item_seleccionada)
    
        try:
            self.ventana_cancion_playlist.ventana_de_playlist.ventana_principal.software.agregar_cancion_a_la_playlist(self.playlist, cancion_seleccionada)
        except Exception as e:
            mensaje_de_excepcion = "Ocurrió un error al agregar la canción a la playlist: " + str(e)
            messagebox.showinfo("Error", mensaje_de_excepcion)
        
    
        self.ventana_cancion_playlist.cargar_canciones()
    
    def mostrar(self):
        self.ventana.mainloop()