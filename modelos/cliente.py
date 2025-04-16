from .usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id_usuario, nombre, apellido, correo, telefono, membresia_tipo, fecha_inicio_membresia, estado_membresia):
        super().__init__(id_usuario, nombre, apellido, correo, telefono)
        self.membresia_tipo = membresia_tipo
        self.fecha_inicio_membresia = fecha_inicio_membresia
        self.estado_membresia = estado_membresia
