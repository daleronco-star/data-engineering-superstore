# Importiamo le librerie necessarie

import logging
from pathlib import Path

# Individuiamo la cartella principale del progetto

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Definiamo la cartella dei log

LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Definiamo il percorso del file di log

LOG_FILE = LOG_DIR / "pipeline.log"

# Configuriamo il sistema di logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

# Creiamo il logger del progetto

logger = logging.getLogger("data_engineering")