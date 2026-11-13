class ErrorSistema(Exception):
    """Error general del sistema."""

class DatoIncorrecto(ErrorSistema):
    pass

class ServicioNoDisponible(ErrorSistema):
    pass

class ReservaIncorrecta(ErrorSistema):
    pass
