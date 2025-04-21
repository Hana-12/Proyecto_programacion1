from .usuario import Usuario
import hashlib
import re

class Empleado(Usuario):
    """
    Representa a un empleado del gimnasio.

    Hereda de la clase Usuario y añade información específica del empleado como 
    rol, credenciales de acceso, fecha de contratación y salario.

    Attributes:
        rol (str): Rol del empleado (administrador, instructor, aseo, etc.).
        usuario_login (str): Nombre de usuario para iniciar sesión.
        fecha_contratacion (str): Fecha en que fue contratado.
        __contrasena (str): Contraseña del empleado (privado).
        __salario (float): Salario mensual del empleado (privado).
    """

    def __init__(self, id_usuario, nombre, apellido, correo, telefono, 
                 rol, usuario_login, contrasena, fecha_contratacion, salario):
        """
        Inicializa un objeto Empleado con atributos heredados y propios.

        Args:
            id_usuario (int): Identificador único del empleado.
            nombre (str): Nombre del empleado.
            apellido (str): Apellido del empleado.
            correo (str): Correo electrónico del empleado.
            telefono (str): Número de teléfono del empleado.
            rol (str): Rol dentro del gimnasio.
            usuario_login (str): Usuario asignado para el inicio de sesión.
            contrasena (str): Contraseña del empleado.
            fecha_contratacion (str): Fecha de contratación.
            salario (float): Salario del empleado.
        """
        super().__init__(id_usuario, nombre, apellido, correo, telefono)
        self.rol = rol
        self.usuario_login = usuario_login
        self.fecha_contratacion = fecha_contratacion
        self.__salario = salario
        self.set_contrasena(contrasena)  # Aplica validación y hashing
    
    def __str__(self):
        """
        Representación en cadena del empleado.

        Returns:
            str: Nombre, id y rol en formato legible.
        """
        return f"{self.nombre} ({self.id_usuario}) - {self.rol}"

    def get_salario(self):
        """Retorna el salario del empleado."""
        return self.__salario

    def set_salario(self, nuevo_salario):
        """
        Modifica el salario del empleado si el valor es válido.

        Args:
            nuevo_salario (float): Nuevo valor para el salario.

        Raises:
            ValueError: Si el salario es negativo.
        """
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = nuevo_salario


    def set_contrasena(self, nueva_contrasena):
        """
        Valida y almacena una contraseña segura con hashing SHA-256.

        Args:
            nueva_contrasena (str): Nueva contraseña en texto plano.

        Raises:
            ValueError: Si no cumple con los requisitos mínimos de seguridad.
        """
        if not self.__validar_contrasena_segura(nueva_contrasena):
            raise ValueError(
                "La contraseña debe tener al menos 8 caracteres, una mayúscula, "
                "una minúscula, un número y un carácter especial."
            )
        self.__contrasena_hash = self.__hash_contrasena(nueva_contrasena)

    def verificar_contrasena(self, contrasena_ingresada):
        """
        Verifica si la contraseña ingresada coincide con la almacenada.

        Args:
            contrasena_ingresada (str): Contraseña en texto plano.

        Returns:
            bool: True si coincide, False en caso contrario.
        """
        return self.__hash_contrasena(contrasena_ingresada) == self.__contrasena_hash
    
    
    def __hash_contrasena(self, contrasena):
        """Devuelve el hash SHA-256 de una contraseña."""
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

    def __validar_contrasena_segura(self, contrasena):
        """Valida que la contraseña cumpla criterios de seguridad mínima."""
        return (
            len(contrasena) >= 8 and
            re.search(r'[A-Z]', contrasena) and
            re.search(r'[a-z]', contrasena) and
            re.search(r'[0-9]', contrasena) and
            re.search(r'[^A-Za-z0-9]', contrasena)
        )
    def mostrar_informacion(self):
        """
        Devuelve una representación detallada del empleado.

        Returns:
            str: Rol y salario del empleado.
        """
        return (f"Empleado: {self.nombre} {self.apellido} | Rol: {self.rol} | "
                f"Salario: ${self.get_salario():,.2f}")