from .usuario import Usuario

class Empleado(Usuario):
    def __init__(self, id_usuario, nombre, apellido, correo, telefono, rol, usuario_login, contrasena, fecha_contratacion, salario):
        super().__init__(id_usuario, nombre, apellido, correo, telefono)
        self.rol = rol
        self.usuario_login = usuario_login
        self.contrasena = contrasena
        self.fecha_contratacion = fecha_contratacion
        self.salario = salario
