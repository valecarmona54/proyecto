class Cancion:
    def __init__(self, parametro_nombre_cancion: str, direccion_archivo: str):
        self.nombre_cancion = parametro_nombre_cancion
        self.direccion_archivo = direccion_archivo

    def __str__(self) -> str:
        return self.nombre_cancion