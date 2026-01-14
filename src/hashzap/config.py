import os
import logging
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
    FLET_PORT = int(os.getenv("FLET_PORT", 8000))


# Configuração básica de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("Hashzap")
