
from kaqj.config.settings import KAQJSettings


def test_application_settings():
    assert KAQJSettings.APP_NAME == "KAQJ"
    assert KAQJSettings.VERSION == "0.1.0"
    assert KAQJSettings.DEBUG is False
    assert KAQJSettings.DEFAULT_MODEL is None
    assert KAQJSettings.AI_BASE_URL == "http://localhost:11434"
