from abc import ABC, abstractmethod
from .exceptions import DatoIncorrecto, ServicioNoDisponible, ReservaIncorrecta
from .logs import crear_log

log = crear_log()


class Entidad(ABC):
    """Clase general para las entidades del programa."""

    def __init__(self, codigo):
        if codigo == "":
            raise DatoIncorrecto("El código no puede estar vacío")
        self.codigo = codigo

    @abstractmethod
    def mostrar_datos(self):
        pass


class Cliente(Entidad):
    def __init__(self, codigo, nombre, correo, telefono):
        super().__init__(codigo)

        if nombre == "":
            raise DatoIncorrecto("El nombre es obligatorio")
        if "@" not in correo or "." not in correo:
            raise DatoIncorrecto("El correo no es válido")
        if len(str(telefono)) < 7:
            raise DatoIncorrecto("El teléfono debe tener mínimo 7 números")

        # Los datos se guardan con guion bajo para mantenerlos encapsulados.
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    def mostrar_datos(self):
        return f"{self.codigo} - {self.nombre} - {self.correo}"


class Servicio(ABC):
    def __init__(self, codigo, nombre, precio):
        if precio <= 0:
            raise DatoIncorrecto("El precio debe ser mayor que cero")
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, horas, **datos):
        pass

    @abstractmethod
    def validar(self, horas, **datos):
        pass

    @abstractmethod
    def mostrar_datos(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, codigo, nombre, precio, capacidad):
        super().__init__(codigo, nombre, precio)
        self.capacidad = capacidad

    def validar(self, horas, **datos):
        if not self.disponible:
            raise ServicioNoDisponible("La sala no está disponible")
        personas = datos.get("personas", 1)
        if horas <= 0:
            raise DatoIncorrecto("Las horas deben ser mayores que cero")
        if personas <= 0 or personas > self.capacidad:
            raise DatoIncorrecto("La cantidad de personas no es válida")

    def calcular_costo(self, horas, **datos):
        self.validar(horas, **datos)
        impuesto = datos.get("impuesto", 0)
        descuento = datos.get("descuento", 0)
        total = self.precio * horas
        total = total - (total * descuento)
        total = total + (total * impuesto)
        return round(total, 2)

    def mostrar_datos(self):
        return f"Sala: {self.nombre}, capacidad: {self.capacidad}"


class AlquilerEquipo(Servicio):
    def __init__(self, codigo, nombre, precio, cantidad):
        super().__init__(codigo, nombre, precio)
        self.cantidad = cantidad

    def validar(self, horas, **datos):
        if not self.disponible:
            raise ServicioNoDisponible("El equipo no está disponible")
        unidades = datos.get("unidades", 1)
        if horas <= 0 or unidades <= 0:
            raise DatoIncorrecto("Las horas y unidades deben ser positivas")
        if unidades > self.cantidad:
            raise ServicioNoDisponible("No hay suficientes equipos")

    def calcular_costo(self, horas, **datos):
        self.validar(horas, **datos)
        unidades = datos.get("unidades", 1)
        impuesto = datos.get("impuesto", 0)
        total = self.precio * horas * unidades
        return round(total + total * impuesto, 2)

    def mostrar_datos(self):
        return f"Equipo: {self.nombre}, unidades: {self.cantidad}"


class Asesoria(Servicio):
    def __init__(self, codigo, nombre, precio, tema):
        super().__init__(codigo, nombre, precio)
        self.tema = tema

    def validar(self, horas, **datos):
        if not self.disponible:
            raise ServicioNoDisponible("La asesoría no está disponible")
        if horas <= 0 or horas > 8:
            raise DatoIncorrecto("La asesoría debe durar entre 1 y 8 horas")

    def calcular_costo(self, horas, **datos):
        self.validar(horas, **datos)
        impuesto = datos.get("impuesto", 0)
        total = self.precio * horas
        return round(total + total * impuesto, 2)

    def mostrar_datos(self):
        return f"Asesoría: {self.nombre}, tema: {self.tema}"


class Reserva(Entidad):
    def __init__(self, codigo, cliente, servicio, horas, **datos):
        super().__init__(codigo)
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.datos = datos
        self.estado = "Pendiente"
        self.total = 0

    def confirmar(self, impuesto=0, descuento=0):
        if self.estado != "Pendiente":
            raise ReservaIncorrecta("La reserva no está pendiente")

        try:
            # Se usan los mismos métodos, pero cada servicio calcula a su manera.
            self.total = self.servicio.calcular_costo(
                self.horas,
                **self.datos,
                impuesto=impuesto,
                descuento=descuento
            )
            self.estado = "Confirmada"
            log.info("Reserva %s confirmada", self.codigo)
            return self.total

        except Exception as error:
            self.estado = "Fallida"
            log.exception("No se pudo confirmar la reserva %s", self.codigo)
            # Se conserva el error original como causa.
            raise ReservaIncorrecta("No se pudo confirmar la reserva") from error

    def cancelar(self):
        if self.estado != "Confirmada":
            raise ReservaIncorrecta("Solo se cancelan reservas confirmadas")
        self.estado = "Cancelada"
        log.info("Reserva %s cancelada", self.codigo)

    def procesar(self):
        try:
            resultado = self.confirmar()
        except ReservaIncorrecta as error:
            print("Error controlado:", error)
            return False
        else:
            print("Reserva procesada. Total:", resultado)
            return True
        finally:
            log.info("Terminó el proceso de reserva %s", self.codigo)

    def mostrar_datos(self):
        return (f"Reserva {self.codigo} - Cliente: {self.cliente.nombre} - "
                f"Servicio: {self.servicio.nombre} - Estado: {self.estado}")
