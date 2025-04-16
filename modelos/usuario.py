class Usuario:
    def __init__(self, id_usuario, nombre, apellido, correo, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido} (ID: {self.id_usuario})"
