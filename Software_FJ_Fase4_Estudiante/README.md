# Proyecto Software FJ - Fase 4

Este proyecto es una aplicación sencilla en Python para manejar clientes, servicios y reservas de la empresa Software FJ.

## Cómo ejecutar
1. Tener instalado Python 3.
2. Abrir esta carpeta en Visual Studio Code.
3. Abrir la terminal.
4. Escribir:

   `python main.py`

No se necesitan instalar paquetes adicionales.

## Archivos
- `main.py`: tiene las pruebas del programa.
- `software_fj/clases.py`: contiene las clases Cliente, Servicio, Reserva y los servicios.
- `software_fj/gestor.py`: guarda los datos en listas.
- `software_fj/exceptions.py`: contiene los errores personalizados.
- `software_fj/logs.py`: crea el archivo donde se guardan los eventos y errores.
- `logs/registro.txt`: aparece después de ejecutar el programa.

## Qué se trabaja
Se usan clases abstractas, herencia, encapsulación y polimorfismo. También se hacen validaciones y se manejan errores con try y except. Las reservas se guardan en listas, no en una base de datos.

El programa muestra 14 operaciones de ejemplo, algunas correctas y otras con errores para comprobar que no se cierre cuando ocurre un problema.
