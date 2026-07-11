import os

from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


class Settings:
    """
    Application configuration.
    Reads values from the .env file.
    """

    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    DEBUG = os.getenv("DEBUG")

    DATABASE_URL = os.getenv("DATABASE_URL")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Create one global settings object
settings = Settings()