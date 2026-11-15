
import os

from dotenv import load_dotenv

load_dotenv()


class KAQJSettings:
    """Application settings for KAQJ."""

    APP_NAME = "KAQJ"
    VERSION = "0.1.0"

    DEBUG = os.getenv("KAQJ_DEBUG", "false").lower() == "true"

    DEFAULT_MODEL = os.getenv("KAQJ_DEFAULT_MODEL") or None

    AI_BASE_URL = os.getenv(
        "KAQJ_AI_BASE_URL",
        "http://localhost:11434",
    )
