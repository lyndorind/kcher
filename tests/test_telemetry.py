import logging

from k_cher.logging_config import setup_logging


def test_creating_calculation_writes_info_log(client, caplog):
    with caplog.at_level(logging.INFO, logger="k_cher"):
        response = client.post(
            "/calculations", json={"operation": "add", "a": 1, "b": 2}
        )

    assert response.status_code == 201
    assert "Calculation saved" in caplog.text


def test_rejected_calculation_writes_warning_log(client, caplog):
    with caplog.at_level(logging.WARNING, logger="k_cher"):
        response = client.post(
            "/calculations", json={"operation": "divide", "a": 1, "b": 0}
        )

    assert response.status_code == 400
    assert "division_by_zero" in caplog.text


def test_setup_logging_is_idempotent():
    package_logger = logging.getLogger("k_cher")
    handlers_before = len(package_logger.handlers)

    setup_logging()
    setup_logging()

    assert len(package_logger.handlers) == handlers_before
    assert package_logger.level == logging.INFO
