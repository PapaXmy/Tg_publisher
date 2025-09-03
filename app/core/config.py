# конфигурации

from pydantic_settings import BaseSetting


class Settings(BaseSetting):
    PROJECT_NAME: str = "TG_publisher"
    DEBUG: bool = True

    # database

    POSTGRES_USER: str = "tg_publisher_user"
    POSTGRES_PASSWORD: str = "tg_publisher_password"
    POSTGRES_DB: str = "tg_publisher_bot"
    POSTGRES_HOST: str = "locahost"
    POSTGRES_PORT: int = 5432

    DATABASE_URL: str | None = None

    # security
    SECRET_KEY: str = "supersecret"
    ALGORITHM: str = "HS256"
    ACCSESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

    @property
    def db_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()
