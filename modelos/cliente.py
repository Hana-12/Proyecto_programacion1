from .usuario import Usuario

class Cliente(Usuario):
    """
    Representa a un cliente del gimnasio.

    Hereda de la clase Usuario y añade información relacionada con la membresía 
    del cliente, como tipo, fecha de inicio y estado actual.

    Attributes:
        membresia_tipo (str): Tipo de membresía (mensual, trimestral, anual).
        fecha_inicio_membresia (str): Fecha de inicio de la membresía.
        __estado_membresia (str): Estado actual de la membresía (encapsulado).
    """

    def __init__(self, id_usuario, nombre, apellido, correo, telefono, 
                 membresia_tipo, fecha_inicio_membresia, estado_membresia):
        """
        Inicializa un objeto Cliente con los datos personales y de membresía.

        Args:
            id_usuario (int): Identificador único del cliente.
            nombre (str): Nombre del cliente.
            apellido (str): Apellido del cliente.
            correo (str): Correo electrónico del cliente.
            telefono (str): Número de teléfono.
            membresia_tipo (str): Tipo de membresía.
            fecha_inicio_membresia (str): Fecha de inicio de la membresía.
            estado_membresia (str): Estado inicial de la membresía.
        """
        super().__init__(id_usuario, nombre, apellido, correo, telefono)
        self.membresia_tipo = membresia_tipo
        self.fecha_inicio_membresia = fecha_inicio_membresia
        self.set_estado_membresia(estado_membresia)  # Usa setter para validación

    def __str__(self):
        """
        Representación en cadena del cliente.

        Returns:
            str: Nombre, id y membresia en formato legible.
        """
        return f"{self.nombre} ({self.id_usuario}) - {self.membresia_tipo}"


    def get_estado_membresia(self):
        """
        Retorna el estado actual de la membresía.

        Returns:
            str: Estado de la membresía ("activa" o "inactiva").
        """
        return self.__estado_membresia

    def set_estado_membresia(self, nuevo_estado):
        """
        Establece el estado de la membresía si es válido.

        Args:
            nuevo_estado (str): Nuevo estado a asignar.

        Raises:
            ValueError: Si el estado no es "activa" ni "inactiva".
        """
        if nuevo_estado.lower() not in ("activa", "inactiva"):
            raise ValueError("El estado de la membresía debe ser 'activa' o 'inactiva'.")
        self.__estado_membresia = nuevo_estado.lower()
    def mostrar_informacion(self):
        """
        Devuelve una representación detallada del cliente.

        Returns:
            str: Información de membresía y estado.
        """
        return (f"Cliente: {self.nombre} {self.apellido} | "
                f"Membresía: {self.membresia_tipo} | Estado: {self.get_estado_membresia()}")
