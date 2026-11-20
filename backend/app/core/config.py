from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Stock Analysis Platform"
    DEBUG: bool = True

    DATABASE_URL: str
    TWELVE_DATA_API_KEY: str = ""

    CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    CACHE_TTL_MINUTES: int = 60

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()