# Informe Final - Sistema de Gestión de Gimnasio

Este proyecto implementa un sistema básico de gestión para un gimnasio, utilizando Python y principios de Programación Orientada a Objetos (POO). El sistema permite administrar empleados, clientes y máquinas, proporcionando funcionalidades para registrar, eliminar, modificar y listar información.

## Estudiantes
Los estudiantes que pertenecemos al grupo somos:

* Camilo Andrés De la Cruz Arboleda
* Diana Carolina Ospina Ocampo
* Hana Carolina Niño Mora
* Jean Pierre Villamil Sanchez
* Sandra Milena Campos Gonzalez

## Características Principales

## Gestión de Empleados:
    * Registro de nuevos empleados con información como ID, nombre, apellido, correo, teléfono, rol, usuario de login, contraseña, fecha de contratación y salario.
    * Eliminación de empleados por ID. 
    * Modificación del salario y teléfono de los empleados. 
## Gestión de Clientes:
    * Registro de nuevos clientes con información como ID, nombre, apellido, correo, teléfono, tipo de membresía, fecha de inicio de membresía y estado de la membresía.
    * Eliminación de clientes por ID. 
## Gestión de Máquinas:
    * Registro de nuevas máquinas con información como ID, nombre, tipo, marca, estado, fecha de adquisición y ubicación.
    * Eliminación de máquinas por ID.
## Listado de Información:
    * Capacidad de listar todos los empleados, clientes y máquinas registrados en el sistema. [cite: 8]
## Validaciones:
    * Validación de formato de correo electrónico.
    * Validación de formato de número de teléfono (10 dígitos numéricos). 
## Manejo de Excepciones:
    * Manejo de la excepción `ValueError` para asegurar que las entradas de ID y salario sean numéricas.

## Estructura del Proyecto

El proyecto se organiza en los siguientes archivos:

* `main.py`:  Archivo principal que contiene el menú de la aplicación y la lógica para interactuar con el usuario. 
* `modelos/gimnasio.py`:  Clase `Gimnasio` que gestiona las listas de empleados, clientes y máquinas, y contiene los métodos para realizar las operaciones. 
* `modelos/cliente.py`:  Clase `Cliente` que representa a un cliente del gimnasio. 
* `modelos/empleado.py`:  Clase `Empleado` que representa a un empleado del gimnasio.
* `modelos/maquina.py`:  Clase `Maquina` que representa una máquina del gimnasio. 
* `modelos/usuario.py`: Clase `Usuario` que representa a un usuario genérico (superclase (herencia) de Cliente y Empleado).

## Clases Principales

* `Gimnasio`: Clase principal que coordina todas las operaciones del sistema.
* `Cliente`: Representa a un cliente del gimnasio, heredando de la clase `Usuario`.
* `Empleado`: Representa a un empleado del gimnasio, heredando de la clase `Usuario`.
* `Maquina`: Representa una máquina del gimnasio.
* `Usuario`: Clase base para `Cliente` y `Empleado`, conteniendo atributos comunes. 

## Uso

1.  Ejecute el archivo `main.py`.
2.  Seleccion de un menú de opciones para realizar la operación deseada.
3.  Siga las instrucciones en pantalla.

