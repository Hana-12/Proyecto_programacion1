from modelos.gimnasio import Gimnasio


def mostrar_menu():
    print("""
--- MENÚ DEL GIMNASIO ---
1. Registrar cliente
2. Registrar empleado
3. Registrar máquina
4. Listar clientes
5. Listar empleados
6. Listar máquinas
7. Eliminar cliente
8. Eliminar empleado
9. Eliminar máquina
10. Modificar empleado
11. Generar reporte de clientes
12. Generar reporte de empleados
13. Mostrar información de todos los usuarios
0. Salir
""")


def main():
    gimnasio = Gimnasio()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gimnasio.registrar_cliente()
        elif opcion == "2":
            gimnasio.registrar_empleado()
        elif opcion == "3":
            gimnasio.registrar_maquina()
        elif opcion == "4":
            gimnasio.listar_clientes()
        elif opcion == "5":
            gimnasio.listar_empleados()
        elif opcion == "6":
            gimnasio.listar_maquinas()
        elif opcion == "7":
            gimnasio.eliminar_cliente()
        elif opcion == "8":
            gimnasio.eliminar_empleado()
        elif opcion == "9":
            gimnasio.eliminar_maquina()
        elif opcion == "10":
            gimnasio.modificar_empleado()
        elif opcion == "11":
            gimnasio.generar_reporte("clientes")
        elif opcion == "12":
            gimnasio.generar_reporte("empleados")
        elif opcion == "13":
            gimnasio.mostrar_todos_los_usuarios()
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
