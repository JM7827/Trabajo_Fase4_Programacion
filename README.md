# Proyecto Software FJ - Fase 4

Este proyecto es una aplicacion sencilla en Python para manejar clientes, servicios y reservas de la empresa Software FJ.

## Como ejecutar
1. Tener instalado Python 3.
2. Abrir esta carpeta en Visual Studio Code.
3. Abrir la terminal.
4. Escribir:

   `python main.py`

No se necesitan instalar paquetes adicionales.

## Archivos
- `main.py`: contiene las pruebas del programa y las 15 operaciones de ejemplo.
- `software_fj/clases.py`: contiene las clases Cliente, Servicio, Reserva y los servicios especializados.
- `software_fj/gestor.py`: administra clientes, servicios y reservas mediante listas.
- `software_fj/exceptions.py`: contiene los errores personalizados.
- `software_fj/logs.py`: configura el archivo donde se guardan eventos y errores.
- `logs/registro.txt`: se crea o actualiza despues de ejecutar el programa.

## Que se trabaja
Se usan clases abstractas, herencia, encapsulacion y polimorfismo. Tambien se hacen validaciones y se manejan errores con try, except, else, finally y encadenamiento de excepciones. Las reservas se guardan en listas, no en una base de datos.
