from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "front"
    BACK_URL: str = "http://localhost:8001"
    model_config = {"env_file": ".env"}  # טוען משתני סביבה מ-.env בפיתוח

settings = Settings()
