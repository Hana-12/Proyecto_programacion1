from modelos.gimnasio import Gimnasio

gimnasio = Gimnasio()

def mostrar_menu():
    print("\n--- MENÚ DEL GIMNASIO ---")
    print("1. Registrar empleado")
    print("2. Eliminar empleado")
    print("3. Modificar empleado")
    print("4. Registrar Cliente")
    print("5. Eliminar Cliente")
    print("6. Registrar máquina")
    print("7. Eliminar máquina")
    print("8. Listar empleados")
    print("9. Listar clientes")
    print("10. Listar maquinas")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    try:
        opcion = int(opcion)  # Intentar convertir la entrada a un entero
    except ValueError:
        print("Error: Por favor, ingresa un número de opción válido.")
        continue  # Volver al inicio del bucle

    if opcion == 1:
        gimnasio.registrar_empleado()  # Registrar un empleado
    elif opcion == 2:
        gimnasio.eliminar_empleado()  # Eliminar un empleado
    elif opcion == 3:
        gimnasio.modificar_empleado()  # Modificar un empleado
    elif opcion == 4:
        gimnasio.registrar_cliente()  # Registrar un cliente
    elif opcion == 5:
        gimnasio.eliminar_cliente()  # Eliminar un cliente
    elif opcion == 6:
        gimnasio.registrar_maquina()  # Registrar una máquina
    elif opcion == 7:
        gimnasio.eliminar_maquina()  # Eliminar una máquina
    elif opcion == 8:
        gimnasio.listar_empleados()  # Listar empleados
    elif opcion == 9:
        gimnasio.listar_clientes()  # Listar clientes
    elif opcion == 10:
        gimnasio.listar_maquinas()  # Listar máquinas
    elif opcion == 0:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")