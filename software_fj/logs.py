import logging
from pathlib import Path


def crear_log():
    """Prepara el archivo de registro y devuelve el logger del proyecto."""
    carpeta = Path(__file__).resolve().parent.parent / "logs"
    carpeta.mkdir(exist_ok=True)
    archivo = carpeta / "registro.txt"

    logger = logging.getLogger("software_fj")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Evita crear varios manejadores si se llama la funcion mas de una vez.
    if not logger.handlers:
        manejador = logging.FileHandler(archivo, encoding="utf-8")
        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        manejador.setFormatter(formato)
        logger.addHandler(manejador)

    return logger
