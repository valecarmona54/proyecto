import tkinter 
from tkinter import messagebox
from view.ventana_creacion_playlist import VentanaCreacionPlaylist
from view.ventana_cancion_playlist import VentanaCancionPlaylist


class VentanaDePlaylist:
    def __init__(self, ventana_principal):
        self.ventana_principal =ventana_principal
        self.ventana: tkinter.Tk= tkinter.Tk() #Se llama el metodo constructo de la clase Tk de la libreria tkinter
        self.ventana.title("Playlist")
        self.ventana.geometry("400x400")
        self.BotonVerPlaylist=tkinter.Button(self.ventana, text="Ver lista", command=self.abrir_ventana_ver_playlist)
        self.BotonVerPlaylist.pack()
        self.BotonAgregarPlaylist =tkinter.Button(self.ventana, text="Crear lista", command=self.abrir_ventana_creacion_playlist)
        self.BotonAgregarPlaylist.pack()
        self.listboxDePlaylist = tkinter.Listbox(self.ventana) 
        self.listboxDePlaylist.pack() 


    def abrir_ventana_creacion_playlist(self):
        ventanaCreacionPlaylist = VentanaCreacionPlaylist(self)
        ventanaCreacionPlaylist.mostrar()

    def abrir_ventana_ver_playlist(self):
        indices = self.listboxDePlaylist.curselection()
        if indices:
            selected_index = indices[0]
            selected_playlist = self.ventana_principal.software.listas_de_reproduccion[selected_index]
            ventanaCancionPlaylist = VentanaCancionPlaylist(self, selected_playlist)
            ventanaCancionPlaylist.mostrar()
        else:
            messagebox.showinfo("Error", "Selecciona una lista de reproducción primero.")
        
    
    def actualizar_lista_de_playlist(self):
        self.listboxDePlaylist.delete(tkinter.END)
        for playlist in self.ventana_principal.software.listas_de_reproduccion: #Catalogo de software
            self.listboxDePlaylist.insert(tkinter.END, playlist.nombre_lista)

    def mostrar(self):
        self.ventana.mainloop()
