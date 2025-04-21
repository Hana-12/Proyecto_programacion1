from .cliente import Cliente
from .empleado import Empleado
from .maquina import Maquina
from .utilities import validar_correo, validar_telefono
from .reporte_generadores import ReporteClientes, ReporteEmpleados


class Gimnasio:
    """
    Representa el sistema de gestión de un gimnasio.

    Esta clase centraliza la administración de usuarios, empleados y máquinas.
    Permite registrar, modificar, eliminar y listar cada uno de estos elementos,
    además de manejar la asignación automática de IDs.

    Attributes:
        usuarios (list): Lista de objetos Cliente registrados en el sistema.
        empleados (list): Lista de objetos Empleado registrados.
        maquinas (list): Lista de objetos Maquina disponibles en el gimnasio.
        next_usuario_id (int): ID incremental para el registro de nuevos clientes.
        next_empleado_id (int): ID incremental para el registro de nuevos empleados.
        next_maquina_id (int): ID incremental para el registro de nuevas máquinas.
    """
    def __init__(self):
        self.usuarios = []
        self.empleados = []
        self.maquinas = []
        self.next_usuario_id = 1
        self.next_empleado_id = 1
        self.next_maquina_id = 1

#Registrar empleado

    def registrar_empleado(self):
        """
        Registra un nuevo empleado en el sistema.

        Solicita al usuario los datos del nuevo empleado, incluyendo nombre, apellido, 
        correo (validado), teléfono (validado), rol, contraseña, fecha de contratación 
        y salario (validado como número). Verifica que no exista un empleado con el mismo 
        correo antes de registrarlo. Asigna un ID único al nuevo empleado y lo agrega a 
        la lista `self.empleados`.

        Roles válidos: administrador, instructor, aseo.

        Returns:
            None
        """
        print("Registro de nuevo empleado:")
        id_usuario = self.next_empleado_id
        self.next_empleado_id += 1
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        while True:
            correo = input("Correo: ")
            if validar_correo(correo):
                break
            else:
                print("Correo inválido. Debe contener un solo '@' y dominio válido.")

        while True:
            telefono = input("Teléfono (10 digitos): ")
            if validar_telefono(telefono):
                break
            else:
                print("Teléfono inválido. Debe ser numérico y contener exactamente 10 números.")

        for empleado in self.empleados:
            if empleado.correo == correo:
                print("Error: Ya existe un empleado registrado con ese correo.")
                print("Por favor, modifique la información del empleado existente.")
                return

        rol = input("Rol (administrador, instructor, aseo): ")
        usuario_login = correo
        fecha_contratacion = input("Fecha de contratación: DD/MM/AAAA ")
        
        try:
            salario = float(input("Salario: "))
        except ValueError:
            print("Error: El salario debe ser un número válido.")
            return
        
        while True:
            contrasena = input("Contraseña: ")
            try:
                empleado = Empleado(id_usuario, nombre, apellido, correo, 
                                    telefono, rol, usuario_login, contrasena, 
                                    fecha_contratacion, salario)
                break  # Salimos del bucle si no lanza excepción
            except ValueError as e:
                print(f"Error en la contraseña: {e}")


        empleado = Empleado(id_usuario, nombre, apellido, correo, 
                            telefono, rol, usuario_login, contrasena, 
                            fecha_contratacion, salario)
        self.empleados.append(empleado)
        print(f"Empleado registrado correctamente. Con ID {id_usuario} y usuario login {correo}")

#Eliminar empleado

    def eliminar_empleado(self):
        """
        Elimina un empleado del sistema según su ID.

        Solicita al usuario el ID del empleado que desea eliminar.
        Valida que el ID sea un número entero. Luego filtra la lista 
        `self.empleados` para eliminar al empleado con ese ID.

        Returns:
            None
        """
        try:
            id_usuario = int(input("ID del empleado a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero válido.")
            return
        self.empleados = [e for e in self.empleados if e.id_usuario != id_usuario]
        print(f"Empleado con ID {id_usuario} eliminado.")

#modificar empleado

    def modificar_empleado(self):
        """
        Modifica los datos de un empleado registrado en el sistema.

        Solicita el ID del empleado a modificar. Si se encuentra, permite actualizar 
        el salario (validado como número flotante) y el número de teléfono (validado con 
        formato de 10 dígitos). Si el ID no existe, informa que el empleado no fue encontrado.

        Returns:
            None
        """
        try:
            id_usuario = int(input("ID del empleado a modificar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero válido.")
            return
        for empleado in self.empleados:
            if empleado.id_usuario == id_usuario:
                try:
                    nuevo_salario = float(input("Nuevo salario: "))
                except ValueError:
                    print("Error: El salario debe ser un número válido.")
                    return
                nuevo_telefono = input("Nuevo teléfono (10 digitos): ")
                if validar_telefono(nuevo_telefono):
                    empleado.salario = nuevo_salario
                    empleado.telefono = nuevo_telefono
                    print("Empleado modificado correctamente.")
                else:
                    print("Teléfono inválido. Modificación cancelada.")
                return
        print("Empleado no encontrado.")

#Registrar cliente

    def registrar_cliente(self):
        """
        Registra un nuevo cliente en el sistema.

        Solicita al usuario la información necesaria para crear un nuevo cliente. 
        Valida que el correo y el número de teléfono tengan el formato correcto. 
        También verifica que no exista ya un cliente con el mismo correo en `self.usuarios`. 
        Asigna un ID único al nuevo cliente y lo agrega a la lista de usuarios.

        Los datos solicitados incluyen:
            - Nombre
            - Apellido
            - Correo (validado)
            - Teléfono (10 dígitos, validado)
            - Tipo de membresía (mensual, trimestral, anual)
            - Fecha de inicio de membresía
            - Estado de la membresía (activa o inactiva)

        Returns:
            None
        """
        print("Registro de nuevo cliente:")
        id_usuario = self.next_usuario_id
        self.next_usuario_id += 1
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        while True:
            correo = input("Correo: ")
            if validar_correo(correo):
                break
            else:
                print("Correo inválido. Debe contener un solo '@' y dominio válido.")

        while True:
            telefono = input("Teléfono (10 digitos): ")
            if validar_telefono(telefono):
                break
            else:
                print("Teléfono inválido. Debe contener exactamente 10 números.")

        for usuario in self.usuarios:
            if usuario.correo == correo:
                print("Error: Ya existe un cliente registrado con ese correo.")
                return

        membresia_tipo = input("Tipo de membresia (mensual/trimestral/anual): ")
        fecha_inicio_membresia = input("Fecha de inicio de membresia:DD/MM/AAAA ")
        estado = input("Estado de la membresia (activa/inactiva): ")

        cliente = Cliente(id_usuario, nombre, apellido, correo, 
                          telefono, membresia_tipo, 
                          fecha_inicio_membresia, estado)
        self.usuarios.append(cliente)
        print(f"Cliente registrado correctamente. Con ID {id_usuario} y usuario login {correo}")

#Eliminar cliente

    def eliminar_cliente(self):
        """
        Elimina un cliente del sistema según su ID.

        Solicita al usuario el ID del cliente que desea eliminar. 
        Valida que el ID ingresado sea un número entero. 
        Luego filtra la lista `self.usuarios` para eliminar al cliente con ese ID.

        Returns:
            None
        """
        try:
            id_usuario = int(input("ID del usuario a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero válido.")
            return
        self.usuarios = [u for u in self.usuarios if u.id_usuario != id_usuario]
        print(f"Usuario con ID {id_usuario} eliminado.")

#Registrar maquinas

    def registrar_maquina(self):
        """
        Registra una nueva máquina en el sistema.

        Solicita al usuario la información necesaria para crear una nueva instancia 
        de la clase `Maquina`, asignándole un ID único. Agrega la máquina creada a 
        la lista `self.maquinas`.

        Los campos solicitados son:
            - Nombre
            - Tipo (fuerza, cardio, multifuncional)
            - Marca
            - Estado (operativa, en mantenimiento, fuera de servicio)
            - Fecha de adquisición
            - Ubicación

        Returns:
            None
        """
        print("Registro de nueva máquina:")
        id_maquina = self.next_maquina_id
        self.next_maquina_id += 1
        nombre = input("Nombre de la máquina: ")
        tipo = input("Tipo (fuerza/cardio/multifuncional): ")
        marca = input("Marca: ")
        estado = input("Estado (operativa/en mantenimiento/fuera de servicio): ")
        fecha = input("Fecha de adquisición: ")
        ubicacion = input("Ubicación: ")

        maquina = Maquina(id_maquina, nombre, tipo, marca, estado, fecha, ubicacion)
        self.maquinas.append(maquina)
        print(f"Máquina registrada correctamente. Con ID {id_maquina}")

#Eliminar maquinas

    def eliminar_maquina(self):
        """
        Elimina una máquina del sistema si existe.

        Solicita al usuario el ID de la máquina que desea eliminar. 
        Valida que el ID ingresado sea un número entero. 
        Si la máquina con ese ID no está registrada, informa al usuario.
        Si existe, la elimina de la lista `self.maquinas`.

        Returns:
            None
        """
        try:
            id_maquina = int(input("ID de la máquina a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero válido.")
            return
        if not any(m.id_maquina == id_maquina for m in self.maquinas):
            print("La máquina no está registrada. No se puede eliminar")
            return

        else:
            self.maquinas = [m for m in self.maquinas if m.id_maquina != id_maquina]
            print(f"Máquina con ID {id_maquina} eliminada.")

#Listar empleados

    def listar_empleados(self):
        """
        Imprime por consola la lista de empleados registrados.

        Muestra un encabezado seguido de cada empleado en la lista `self.empleados`.
        Si no hay empleados registrados, imprime un mensaje indicándolo.

        Returns:
            None
        """
        print("\n--- LISTA DE EMPLEADOS ---")
        if not self.empleados:
            print("No hay empleados registrados.")
        else:
            for empleado in self.empleados:
                print(empleado.mostrar_informacion())

#Listar clientes

    def listar_clientes(self):
        """
        Imprime por consola la lista de clientes registrados.

        Muestra un encabezado seguido de cada cliente en la lista `self.usuarios`.
        Si no hay clientes registrados, imprime un mensaje indicándolo.

        Returns:
            None
        """
        print("\n--- LISTA DE CLIENTES ---")
        if not self.usuarios:
            print("No hay clientes registrados.")
        else:
            for cliente in self.usuarios:
                print(cliente.mostrar_informacion())

#Listar maquinas

    def listar_maquinas(self):
        """
        Imprime por consola la lista de máquinas registradas.

        Muestra un encabezado seguido de cada máquina en la lista `self.maquinas`.
        Si no hay máquinas registradas, imprime un mensaje indicándolo.

        Returns:
            None
        """
        print("\n--- LISTA DE MÁQUINAS ---")
        if not self.maquinas:
            print("No hay máquinas registradas.")
        else:
            for maquina in self.maquinas:
                print(maquina)

# Mostrar todos los usuarios para evidenciar
# El polimorfismo

    def mostrar_todos_los_usuarios(self):
        """
        Muestra información de todos los usuarios registrados, tanto empleados como clientes,
        aprovechando el polimorfismo.

        Returns:
            None
        """
        print("\n--- INFORMACIÓN DE TODOS LOS USUARIOS ---")
        if not self.usuarios and not self.empleados:
            print("No hay usuarios ni empleados registrados.")
            return

        for persona in self.usuarios + self.empleados:
            print(persona.mostrar_informacion())

    def generar_reporte(self, tipo):
        """
        Genera un reporte de clientes o empleados según el tipo solicitado.

        Args:
            tipo (str): Puede ser "clientes" o "empleados".

        Returns:
            None
        """
        if tipo == "clientes":
            reporte = ReporteClientes(self.usuarios)
        elif tipo == "empleados":
            reporte = ReporteEmpleados(self.empleados)
        else:
            print("Tipo de reporte no válido.")
            return

        reporte.generar()

