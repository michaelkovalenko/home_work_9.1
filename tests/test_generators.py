import pytest

from src.generators import filter_by_currency


def test_filter_by_currency_valid(transactions_valid_input: list[dict], transactions_result_usd: list[dict]):
    """Проверка фильтрации транзакций по валюте USD (позитивный сценарий)."""
    it = filter_by_currency(transactions_valid_input, "USD")
    for expected_dict in transactions_result_usd:
        assert next(it) == expected_dict


def test_filter_by_currency_valid_2(transactions_valid_input: list[dict], transactions_result_rub: list[dict]):
    """Проверка фильтрации транзакций по валюте RUB (позитивный сценарий)."""
    it = filter_by_currency(transactions_valid_input, "RUB")
    for expected_dict in transactions_result_rub:
        assert next(it) == expected_dict


def test_filter_by_currency_valid_not_currency(transactions_valid_input: list[dict]):
    """Проверка поведения генератора при поиске отсутствующей валюты (EUR)."""
    it = filter_by_currency(transactions_valid_input, "EUR")
    with pytest.raises(StopIteration):
        next(it)


def test_filter_by_currency_invalid_transactions(transactions_invalid_input: list[dict]):
    """Проверка устойчивости генератора к некорректным (грязным) структурам данных."""
    it = filter_by_currency(transactions_invalid_input, "USD")
    with pytest.raises(StopIteration):
        next(it)


def test_filter_by_currency_empty_transaction():
    """Проверка работы генератора с абсолютно пустым входным списком."""
    it = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(it)
