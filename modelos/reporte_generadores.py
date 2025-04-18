from abc import ABC, abstractmethod

class GeneradorReporte(ABC):
    """
    Clase abstracta base para todos los reportes del gimnasio.
    """

    @abstractmethod
    def generar(self):
        """
        Método que debe implementar cada subclase para generar su propio reporte.

        Returns:
            None
        """
        pass


class ReporteClientes(GeneradorReporte):
    def __init__(self, clientes):
        self.clientes = clientes

    def generar(self):
        print("\n--- REPORTE DE CLIENTES ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente.mostrar_informacion())


class ReporteEmpleados(GeneradorReporte):
    def __init__(self, empleados):
        self.empleados = empleados

    def generar(self):
        print("\n--- REPORTE DE EMPLEADOS ---")
        if not self.empleados:
            print("No hay empleados registrados.")
        else:
            for empleado in self.empleados:
                print(empleado.mostrar_informacion())
