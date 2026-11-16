from software_fj.clases import Cliente, ReservaSala, AlquilerEquipo, Asesoria, Reserva
from software_fj.gestor import Gestor
from software_fj.exceptions import DatoIncorrecto, ReservaIncorrecta
from software_fj.logs import crear_log


def ejecutar():
    log = crear_log()
    log.info("Inicio del sistema Software FJ")
    sistema = Gestor()

    print("======================================")
    print("       SISTEMA DE SOFTWARE FJ")
    print("======================================")

    # 1. Registrar un cliente.
    cliente1 = Cliente("C01", "Laura Gomez", "laura@gmail.com", "3001234567")
    sistema.agregar_cliente(cliente1)
    log.info("Operacion 1: cliente C01 registrado")
    print("1. Cliente registrado:", cliente1.mostrar_datos())

    # 2. Registrar otro cliente.
    cliente2 = Cliente("C02", "Carlos Perez", "carlos@gmail.com", "3017654321")
    sistema.agregar_cliente(cliente2)
    log.info("Operacion 2: cliente C02 registrado")
    print("2. Segundo cliente registrado:", cliente2.mostrar_datos())

    # 3. Probar un cliente con datos incorrectos.
    try:
        cliente_malo = Cliente("C03", "", "correo", "123")
        sistema.agregar_cliente(cliente_malo)
    except DatoIncorrecto as error:
        log.error("Operacion 3: cliente incorrecto: %s", error)
        print("3. Cliente incorrecto:", error)
    else:
        log.info("Operacion 3: el cliente de prueba fue aceptado")

    # 4. Probar un cliente repetido.
    try:
        repetido = Cliente("C01", "Otra persona", "otra@gmail.com", "3021234567")
        sistema.agregar_cliente(repetido)
    except DatoIncorrecto as error:
        log.error("Operacion 4: cliente repetido: %s", error)
        print("4. Cliente repetido:", error)
    else:
        log.info("Operacion 4: el cliente no estaba repetido")

    # 5. Crear los tres servicios pedidos en el anexo.
    sala = ReservaSala("S01", "Sala de reuniones", 50000, 12)
    equipo = AlquilerEquipo("S02", "Proyector", 30000, 5)
    asesoria = Asesoria("S03", "Asesoria tecnologica", 80000, "Tecnologia")

    sistema.agregar_servicio(sala)
    sistema.agregar_servicio(equipo)
    sistema.agregar_servicio(asesoria)
    log.info("Operacion 5: se crearon los tres servicios")

    print("5. Servicios creados:")
    for servicio in sistema.servicios:
        print("   ", servicio.mostrar_datos())

    # 6. Intentar crear un servicio con precio incorrecto.
    try:
        servicio_malo = ReservaSala("S04", "Sala pequeña", -5000, 5)
        sistema.agregar_servicio(servicio_malo)
    except DatoIncorrecto as error:
        log.error("Operacion 6: servicio incorrecto: %s", error)
        print("6. Servicio incorrecto:", error)
    else:
        log.info("Operacion 6: el servicio de prueba fue aceptado")

    # 7. Crear y confirmar una reserva de sala.
    reserva1 = Reserva("R01", cliente1, sala, 2, personas=8)
    sistema.agregar_reserva(reserva1)
    total_sala = reserva1.confirmar(impuesto=0.19, descuento=0.10)
    log.info("Operacion 7: reserva de sala confirmada")
    print("7. Total reserva de sala:", total_sala)

    # 8. Crear y confirmar alquiler de equipos.
    reserva2 = Reserva("R02", cliente2, equipo, 3, unidades=2)
    sistema.agregar_reserva(reserva2)
    total_equipo = reserva2.confirmar(impuesto=0.19)
    log.info("Operacion 8: alquiler de equipos confirmado")
    print("8. Total alquiler de equipos:", total_equipo)

    # 9. Crear y confirmar una asesoría.
    reserva3 = Reserva("R03", cliente1, asesoria, 2)
    sistema.agregar_reserva(reserva3)
    total_asesoria = reserva3.confirmar()
    log.info("Operacion 9: asesoria confirmada")
    print("9. Total asesoria:", total_asesoria)

    # 10. Intentar una reserva con más personas que la capacidad.
    reserva4 = Reserva("R04", cliente2, sala, 1, personas=20)
    sistema.agregar_reserva(reserva4)
    print("10. Reserva con capacidad incorrecta:")
    reserva4.procesar()

    # 11. Intentar reservar un servicio que no está disponible.
    sala.disponible = False
    reserva5 = Reserva("R05", cliente1, sala, 1, personas=4)
    sistema.agregar_reserva(reserva5)
    print("11. Reserva de sala no disponible:")
    reserva5.procesar()
    sala.disponible = True

    # 12. Cancelar una reserva que sí fue confirmada.
    reserva1.cancelar()
    log.info("Operacion 12: reserva R01 cancelada")
    print("12. Estado despues de cancelar:", reserva1.estado)

    # 13. Intentar cancelar una reserva fallida.
    try:
        reserva4.cancelar()
    except ReservaIncorrecta as error:
        log.error("Operacion 13: cancelacion no permitida: %s", error)
        print("13. Cancelacion no permitida:", error)
    else:
        log.info("Operacion 13: la reserva se pudo cancelar")

    # 14. Hacer otro calculo usando impuesto y descuento.
    # Este bloque muestra try, except, else y finally.
    try:
        total = sala.calcular_costo(
            1,
            personas=5,
            impuesto=0.19,
            descuento=0.05
        )
    except Exception as error:
        log.exception("Operacion 14: error en el calculo")
        print("14. Error en el calculo:", error)
    else:
        log.info("Operacion 14: calculo realizado correctamente")
        print("14. Otro calculo de sala:", total)
        print("El calculo se realizo correctamente.")
    finally:
        log.info("Operacion 14: finalizo el proceso de calculo")
        print("Finalizo la operacion de calculo.")

    # 15. Probar el encadenamiento de excepciones.
    try:
        try:
            numero = int("texto")
        except ValueError as error:
            raise ReservaIncorrecta(
                "No se pudo procesar el dato de la reserva"
            ) from error
    except ReservaIncorrecta as error:
        log.exception("Operacion 15: excepcion encadenada")
        print("15. Error controlado:", error)
        print("Causa original:", error.__cause__)

    print("--------------------------------------")
    print("Clientes:", len(sistema.clientes))
    print("Servicios:", len(sistema.servicios))
    print("Reservas:", len(sistema.reservas))
    print("Los registros estan en la carpeta logs.")
    print("Programa terminado.")
    log.info("Fin del sistema Software FJ")


if __name__ == "__main__":
    ejecutar()
