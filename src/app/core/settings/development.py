from src.app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    title: str = "Pdf Converter"

    class Config(AppSettings.Config):
        env_file = ".env"
