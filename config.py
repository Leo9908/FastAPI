from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Settings(BaseSettings):
    app_name: str = "Personal Blog"
    admin_email: str = 'leandrojdvr@estudiantes.uci.cu'
    items_per_user: int = 50

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')


setting = Settings()
