import logging
from .exceptions import DatoIncorrecto

log = logging.getLogger("software_fj")


class Gestor:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        for guardado in self.clientes:
            if guardado.codigo == cliente.codigo or guardado.correo == cliente.correo:
                raise DatoIncorrecto("El cliente ya esta registrado")
        self.clientes.append(cliente)
        log.info("Cliente agregado: %s", cliente.codigo)

    def agregar_servicio(self, servicio):
        for guardado in self.servicios:
            if guardado.codigo == servicio.codigo:
                raise DatoIncorrecto("El servicio ya existe")
        self.servicios.append(servicio)
        log.info("Servicio agregado: %s", servicio.codigo)

    def agregar_reserva(self, reserva):
        if reserva.cliente not in self.clientes:
            raise DatoIncorrecto("El cliente no esta registrado")
        if reserva.servicio not in self.servicios:
            raise DatoIncorrecto("El servicio no esta registrado")
        self.reservas.append(reserva)
        log.info("Reserva creada: %s", reserva.codigo)
