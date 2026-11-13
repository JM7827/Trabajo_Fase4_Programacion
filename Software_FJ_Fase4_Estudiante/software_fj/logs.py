import logging
from pathlib import Path

def crear_log():
    carpeta = Path(__file__).resolve().parent.parent / "logs"
    carpeta.mkdir(exist_ok=True)
    archivo = carpeta / "registro.txt"

    logging.basicConfig(
        filename=archivo,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        force=True
    )
    return logging
