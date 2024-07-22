import os
from dotenv import load_dotenv
from pathlib import Path

# Определяем путь к .env файлу
env_path = Path('.') / '.env'

# Загружаем переменные окружения из .env файла
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "zapoi"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")  # Убедимся, что это строка
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Создаем объект настроек
settings = Settings()

# Выводим значения переменных для проверки
print(f"POSTGRES_USER: {settings.POSTGRES_USER}")
print(f"POSTGRES_PASSWORD: {settings.POSTGRES_PASSWORD}")
print(f"POSTGRES_SERVER: {settings.POSTGRES_SERVER}")
print(f"POSTGRES_PORT: {settings.POSTGRES_PORT}")
print(f"POSTGRES_DB: {settings.POSTGRES_DB}")
print(f"DATABASE_URL: {settings.DATABASE_URL}")
