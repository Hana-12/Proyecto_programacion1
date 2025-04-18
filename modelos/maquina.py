class Maquina:
    """
    Representa una máquina disponible en el gimnasio.

    Esta clase contiene información sobre el estado, tipo, ubicación y características
    generales de una máquina de entrenamiento.

    Attributes:
        id_maquina (int): Identificador único de la máquina.
        nombre (str): Nombre de la máquina.
        tipo (str): Tipo de máquina (fuerza, cardio, multifuncional).
        marca (str): Marca del fabricante.
        estado (str): Estado actual de la máquina (operativa, en mantenimiento, etc.).
        fecha_adquisicion (str): Fecha en la que se adquirió la máquina.
        ubicacion (str): Ubicación física de la máquina dentro del gimnasio.
    """

    def __init__(self, id_maquina, nombre, tipo, marca, estado, fecha_adquisicion, ubicacion):
        """
        Inicializa una nueva máquina con los datos especificados.

        Args:
            id_maquina (int): Identificador único de la máquina.
            nombre (str): Nombre de la máquina.
            tipo (str): Tipo (fuerza, cardio, multifuncional).
            marca (str): Marca del fabricante.
            estado (str): Estado actual de la máquina.
            fecha_adquisicion (str): Fecha de adquisición.
            ubicacion (str): Ubicación física de la máquina.
        """
        self.id_maquina = id_maquina
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.estado = estado
        self.fecha_adquisicion = fecha_adquisicion
        self.ubicacion = ubicacion

    def __str__(self):
        """
        Representación en cadena de la máquina.

        Returns:
            str: Nombre, tipo y estado de la máquina en formato legible.
        """
        return f"{self.nombre} ({self.tipo}) - {self.estado}"
