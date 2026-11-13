from software_fj.clases import Cliente, ReservaSala, AlquilerEquipo, Asesoria, Reserva
from software_fj.gestor import Gestor
from software_fj.exceptions import DatoIncorrecto, ReservaIncorrecta


def ejecutar():
    sistema = Gestor()

    print("======================================")
    print("       SISTEMA DE SOFTWARE FJ")
    print("======================================")

    # 1. Registrar un cliente.
    cliente1 = Cliente("C01", "Laura Gomez", "laura@gmail.com", "3001234567")
    sistema.agregar_cliente(cliente1)
    print("1. Cliente registrado:", cliente1.mostrar_datos())

    # 2. Registrar otro cliente.
    cliente2 = Cliente("C02", "Carlos Perez", "carlos@gmail.com", "3017654321")
    sistema.agregar_cliente(cliente2)
    print("2. Segundo cliente registrado:", cliente2.mostrar_datos())

    # 3. Probar un cliente con datos incorrectos.
    try:
        cliente_malo = Cliente("C03", "", "correo", "123")
        sistema.agregar_cliente(cliente_malo)
    except DatoIncorrecto as error:
        print("3. Cliente incorrecto:", error)

    # 4. Probar un cliente repetido.
    try:
        repetido = Cliente("C01", "Otra persona", "otra@gmail.com", "3021234567")
        sistema.agregar_cliente(repetido)
    except DatoIncorrecto as error:
        print("4. Cliente repetido:", error)

    # 5. Crear los tres servicios pedidos en el anexo.
    sala = ReservaSala("S01", "Sala de reuniones", 50000, 12)
    equipo = AlquilerEquipo("S02", "Proyector", 30000, 5)
    asesoria = Asesoria("S03", "Asesoria tecnologica", 80000, "Tecnologia")

    sistema.agregar_servicio(sala)
    sistema.agregar_servicio(equipo)
    sistema.agregar_servicio(asesoria)

    print("5. Servicios creados:")
    for servicio in sistema.servicios:
        print("   ", servicio.mostrar_datos())

    # 6. Intentar crear un servicio con precio incorrecto.
    try:
        servicio_malo = ReservaSala("S04", "Sala pequeña", -5000, 5)
        sistema.agregar_servicio(servicio_malo)
    except DatoIncorrecto as error:
        print("6. Servicio incorrecto:", error)

    # 7. Crear y confirmar una reserva de sala.
    reserva1 = Reserva("R01", cliente1, sala, 2, personas=8)
    sistema.agregar_reserva(reserva1)
    print("7. Total reserva de sala:", reserva1.confirmar(impuesto=0.19, descuento=0.10))

    # 8. Crear y confirmar alquiler de equipos.
    reserva2 = Reserva("R02", cliente2, equipo, 3, unidades=2)
    sistema.agregar_reserva(reserva2)
    print("8. Total alquiler de equipos:", reserva2.confirmar(impuesto=0.19))

    # 9. Crear y confirmar una asesoría.
    reserva3 = Reserva("R03", cliente1, asesoria, 2)
    sistema.agregar_reserva(reserva3)
    print("9. Total asesoría:", reserva3.confirmar())

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
    print("12. Estado después de cancelar:", reserva1.estado)

    # 13. Intentar cancelar una reserva fallida.
    try:
        reserva4.cancelar()
    except ReservaIncorrecta as error:
        print("13. Cancelación no permitida:", error)

    # 14. Hacer otro cálculo usando impuesto y descuento.
    print("14. Otro cálculo de sala:",
          sala.calcular_costo(1, personas=5, impuesto=0.19, descuento=0.05))

    print("--------------------------------------")
    print("Clientes:", len(sistema.clientes))
    print("Servicios:", len(sistema.servicios))
    print("Reservas:", len(sistema.reservas))
    print("Los registros están en la carpeta logs.")
    print("Programa terminado.")


if __name__ == "__main__":
    ejecutar()
