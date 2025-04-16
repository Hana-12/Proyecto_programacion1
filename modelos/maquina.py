class Maquina:
    def __init__(self, id_maquina, nombre, tipo, marca, estado, fecha_adquisicion, ubicacion):
        self.id_maquina = id_maquina
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.estado = estado
        self.fecha_adquisicion = fecha_adquisicion
        self.ubicacion = ubicacion

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.estado}"
