"""Налаштування логування застосунку."""

import logging


def setup_logging() -> None:
    """Логи пакета k_cher рівня INFO виводяться в консоль контейнера.

    Записи також потрапляють у кореневий логер, до якого OpenTelemetry
    підключає свій обробник (експорт логів через OTLP).
    """
    package_logger = logging.getLogger("k_cher")
    package_logger.setLevel(logging.INFO)
    if not package_logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
        )
        package_logger.addHandler(handler)
