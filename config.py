from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AcxiomCRM"
    database_url: str = "sqlite:///./acxiomcrm.db"
    secret_key: str = "change-this-secret-key-in-production"
    session_cookie: str = "acxiom_session"
    password_min_length: int = 8
    max_login_attempts: int = 5
    lockout_minutes: int = 15
    class Config:
        env_file = ".env"

settings = Settings()
