class ErrorSistema(Exception):
    """Error general del sistema Software FJ."""


class DatoIncorrecto(ErrorSistema):
    """Se usa cuando un dato ingresado no cumple las validaciones."""
    pass


class ServicioNoDisponible(ErrorSistema):
    """Se usa cuando un servicio no se encuentra disponible."""
    pass


class ReservaIncorrecta(ErrorSistema):
    """Se usa cuando una reserva no se puede crear, confirmar o cancelar."""
    pass
