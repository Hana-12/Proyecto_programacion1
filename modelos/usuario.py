from abc import ABC, abstractmethod

class Usuario(ABC):
    """
    Clase abstracta que representa un usuario del sistema.

    Define los atributos comunes a todos los tipos de usuario y exige que las
    subclases implementen el método mostrar_informacion().

    Esta clase almacena información general de un usuario como nombre, apellido,
    correo electrónico y teléfono. Sirve como clase base para otros tipos de usuarios
    (como clientes o empleados).

    Attributes:
        id_usuario (int): Identificador único del usuario.
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        correo (str): Correo electrónico del usuario.
        telefono (str): Número de teléfono del usuario.
    """

    def __init__(self, id_usuario, nombre, apellido, correo, telefono):
        """
        Inicializa un nuevo objeto Usuario con los datos proporcionados.

        Args:
            id_usuario (int): Identificador único del usuario.
            nombre (str): Nombre del usuario.
            apellido (str): Apellido del usuario.
            correo (str): Correo electrónico.
            telefono (str): Número de teléfono.
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono



    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que debe ser implementado por todas las subclases.

        Returns:
            str: Información detallada del usuario.
        """
        pass