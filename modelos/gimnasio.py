from .cliente import Cliente
from .empleado import Empleado
from .maquina import Maquina

def validar_correo(correo):
    return '@' in correo and correo.count('@') == 1 and correo.split('@')[-1]

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

class Gimnasio:
    def __init__(self):
        self.usuarios = []
        self.empleados = []
        self.maquinas = []
        self.next_usuario_id = 1
        self.next_empleado_id = 1
        self.next_maquina_id = 1

#Registrar empleado

    def registrar_empleado(self):
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
                print("Teléfono inválido. Debe contener exactamente 10 números.")

        for empleado in self.empleados:
            if empleado.correo == correo:
                print("Error: Ya existe un empleado registrado con ese correo.")
                print("Por favor, modifique la información del empleado existente.")
                return

        rol = input("Rol (administrador, instructor, aseo): ")
        usuario_login = correo
        contrasena = input("Contraseña: ")
        fecha_contratacion = input("Fecha de contratación: DD/MM/AAAA ")
        try:
            salario = float(input("Salario: "))
        except ValueError:
            print("Error: El salario debe ser un número válido.")
            return

        empleado = Empleado(id_usuario, nombre, apellido, correo, telefono, rol, usuario_login, contrasena, fecha_contratacion, salario)
        self.empleados.append(empleado)
        print(f"Empleado registrado correctamente. Con ID {id_usuario} y usuario login {correo}")

#Eliminar empleado

    def eliminar_empleado(self):
        try:
            id_usuario = int(input("ID del empleado a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero válido.")
            return
        self.empleados = [e for e in self.empleados if e.id_usuario != id_usuario]
        print(f"Empleado con ID {id_usuario} eliminado.")

#modificar empleado

    def modificar_empleado(self):
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
        fecha_inicio = input("Fecha de inicio de membresia:DD/MM/AAAA ")
        estado = input("Estado de la membresia (activa/inactiva): ")

        cliente = Cliente(id_usuario, nombre, apellido, correo, telefono, membresia_tipo, fecha_inicio, estado)
        self.usuarios.append(cliente)
        print(f"Cliente registrado correctamente. Con ID {id_usuario} y usuario login {correo}")

#Eliminar cliente

    def eliminar_cliente(self):
        try:
            id_usuario = int(input("ID del usuario a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero válido.")
            return
        self.usuarios = [u for u in self.usuarios if u.id_usuario != id_usuario]
        print(f"Usuario con ID {id_usuario} eliminado.")

#Registrar maquinas

    def registrar_maquina(self):
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
        try:
            id_maquina = int(input("ID de la máquina a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero válido.")
            return
        self.maquinas = [m for m in self.maquinas if m.id_maquina != id_maquina]
        print(f"Máquina con ID {id_maquina} eliminada.")

#Listar empleados

    def listar_empleados(self):
        print("\n--- LISTA DE EMPLEADOS ---")
        if not self.empleados:
            print("No hay empleados registrados.")
        else:
            for empleado in self.empleados:
                print(empleado)

#Listar clientes

    def listar_clientes(self):
        print("\n--- LISTA DE CLIENTES ---")
        if not self.usuarios:
            print("No hay clientes registrados.")
        else:
            for cliente in self.usuarios:
                print(cliente)

#Listar maquinas

    def listar_maquinas(self):
        print("\n--- LISTA DE MÁQUINAS ---")
        if not self.maquinas:
            print("No hay máquinas registradas.")
        else:
            for maquina in self.maquinas:
                print(maquina)