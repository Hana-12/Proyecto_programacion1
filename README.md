# Informe Final - Sistema de Gestión de Gimnasio

Este proyecto implementa un sistema básico de gestión para un gimnasio, utilizando Python y principios de Programación Orientada a Objetos (POO). El sistema permite administrar empleados, clientes y máquinas, proporcionando funcionalidades para registrar, eliminar, modificar y listar información.

La explicación detallada de cómo se implementaron los distintos temas se encuentra en el título `Implementación`. 




## Estudiantes
Los estudiantes que pertenecemos al grupo somos:

* Camilo Andrés De la Cruz Arboleda
* Diana Carolina Ospina Ocampo
* Hana Carolina Niño Mora
* Jean Pierre Villamil Sanchez
* Sandra Milena Campos Gonzalez

## Características Principales

### Gestión de Empleados:
*  Registro de nuevos empleados con información como ID, nombre, apellido, correo, teléfono, rol, usuario de login, contraseña, fecha de contratación y salario.
* Eliminación de empleados por ID. 
* Modificación del salario y teléfono de los empleados. 
### Gestión de Clientes:
* Registro de nuevos clientes con información como ID, nombre, apellido, correo, teléfono, tipo de membresía, fecha de inicio de membresía y estado de la membresía.
* Eliminación de clientes por ID. 
### Gestión de Máquinas:
* Registro de nuevas máquinas con información como ID, nombre, tipo, marca, estado, fecha de adquisición y ubicación.
* Eliminación de máquinas por ID.
### Listado de Información:
* Capacidad de listar todos los empleados, clientes y máquinas registrados en el sistema. [cite: 8]
### Validaciones:
* Validación de formato de correo electrónico.
* Validación de formato de número de teléfono (10 dígitos numéricos). 
### Manejo de Excepciones:
* Manejo de la excepción `ValueError` para asegurar que las entradas de ID y salario sean numéricas.
* Excepción personalizada para el tipo de membresía del cliente.

## Estructura del Proyecto

El proyecto se organiza en los siguientes archivos:

* `main.py`:  Archivo principal que contiene el menú de la aplicación y la lógica para interactuar con el usuario. 
* `modelos/gimnasio.py`:  Clase `Gimnasio` que gestiona las listas de empleados, clientes y máquinas, y contiene los métodos para realizar las operaciones. 
* `modelos/cliente.py`:  Clase `Cliente` que representa a un cliente del gimnasio. 
* `modelos/empleado.py`:  Clase `Empleado` que representa a un empleado del gimnasio.
* `modelos/maquina.py`:  Clase `Maquina` que representa una máquina del gimnasio. 
* `modelos/usuario.py`: Clase `Usuario` que representa a un usuario genérico (superclase (herencia) de Cliente y Empleado).
* `modelos/utilities.py`: Almacenamiento de funciones auxiliares y de la excepción personalizada.
* `modelos/reporte_generadores.py`: Clases que ayudan a generar los reportes y a mostrar la utilidad de las clases abstractas.


## Clases Principales

* `Gimnasio`: Clase principal que coordina todas las operaciones del sistema.
* `Cliente`: Representa a un cliente del gimnasio, heredando de la clase `Usuario`.
* `Empleado`: Representa a un empleado del gimnasio, heredando de la clase `Usuario`.
* `Maquina`: Representa una máquina del gimnasio.
* `Usuario`: Clase base para `Cliente` y `Empleado`, conteniendo atributos comunes. 

## Uso

1. Clona este repositorio o descarga los archivos del proyecto.
2. Asegúrate de que la carpeta contenga la siguiente estructura:

proyecto/ 
├── main.py 
└── modelos/ 
    ├── __init__.py 
    ├── cliente.py 
    ├── empleado.py 
    ├── gimnasio.py 
    ├── maquina.py 
    ├── reporte_generadores.py
    ├── usuario.py 
    └── utilities.py
3.  Ejecuta el archivo `main.py`.
4.  Selección de un menú de opciones para realizar la operación deseada.
5.  Sigue las instrucciones en pantalla.


## Implementación

Este proyecto fue desarrollado aplicando los principios fundamentales de la Programación Orientada a Objetos (POO) y siguiendo los ejemplos planteados en clase por la docente. A continuación se describe cómo se implementaron los principales conceptos:

### Encapsulamiento

Se implementa en la clase `Empleado` mediante el uso de atributos privados (`__salario`, `__contrasena_hash`). En lugar de almacenar la contraseña en texto plano, se guarda su representación segura utilizando hashing SHA-256. El acceso está controlado a través de los métodos `set_contrasena()` (que incluye validación de seguridad) y `verificar_contrasena()` (para autenticación).  
En la clase `Cliente`, se encapsula el atributo `__estado_membresia` y se controla su modificación mediante un setter que restringe los valores permitidos.


### Constructores
Todas las clases (`Usuario`, `Cliente`, `Empleado`, `Maquina`) cuentan con constructores (`__init__`) que inicializan los atributos necesarios al momento de crear una instancia. También se gestionan contadores de IDs únicos desde la clase `Gimnasio`.

### Herencia
Las clases `Cliente` y `Empleado` heredan de la clase base `Usuario`, aprovechando atributos comunes como `id_usuario`, `nombre`, `correo`, etc. Esto reduce la duplicación de código y refuerza el diseño jerárquico del sistema.

### Sobreescritura de métodos
Se sobreescribe el método `mostrar_informacion()` en `Cliente` y `Empleado` para personalizar la salida de acuerdo con cada tipo de usuario.

### Polimorfismo
Se utiliza polimorfismo al iterar sobre listas de `Cliente` y `Empleado` (ambos subtipos de `Usuario`) y llamar a `mostrar_informacion()` sin necesidad de conocer la clase exacta. También se aplica al usar la clase abstracta `GeneradorReporte`, de la cual heredan `ReporteClientes` y `ReporteEmpleados`.

### Clases abstractas
La clase `Usuario` fue definida como clase abstracta (`ABC`) con el método abstracto `mostrar_informacion()`, que deben implementar obligatoriamente las subclases. Esto asegura una interfaz común entre tipos de usuario.

### Interfaces (mediante clases abstractas)
Se simula el uso de interfaces con la clase `GeneradorReporte` (abstracta), que obliga a las subclases como `ReporteClientes` y `ReporteEmpleados` a implementar el método `generar()`, permitiendo una estructura flexible para generación de reportes.

### Composición
La clase `Gimnasio` está compuesta por listas de objetos de otras clases (`Cliente`, `Empleado`, `Maquina`), lo que representa una relación “tiene un”. Esta estructura permite que `Gimnasio` orqueste las operaciones del sistema sin heredar directamente de las demás clases.

### Excepciones personalizadas
La clase `Gimnasio` en el método `registrar_cliente` utiliza una excepción personalizada que se dispara cuando la opción ingresada no está dentro de las opciones. Se utiliza una función `validar_opciones` que retorta True cuando es una opción correcta o dispara la excepción personalizada en caso contrario.

## Futuras versiones

En posteriores desarrollos del aplicativo se podrían agregar validadores adicionales, como a las fechas y a las opciones de ciertos registros.

De igual manera se buscaría que la información fuera persistente, almacenando la data en archivos, para que cuando se cierre y se vuelva a iniciar el programa, la data se mantenga. 

