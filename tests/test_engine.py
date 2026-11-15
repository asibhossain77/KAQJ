
from kaqj.core.engine import KAQJEngine


def test_engine_initialization():
    engine = KAQJEngine()

    assert engine.name == "KAQJ"
    assert engine.version == "0.1.0"
    assert engine.status == "initialized"


def test_engine_get_status():
    engine = KAQJEngine()

    status = engine.get_status()

    assert status == {
        "name": "KAQJ",
        "version": "0.1.0",
        "status": "initialized",
    }
