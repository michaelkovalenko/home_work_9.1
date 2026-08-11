import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_valid_default(banking_operations_valid: list[dict]):
    """Проверяет работу функции в позитивном сценарии с ключом по умолчанию"""
    assert filter_by_state(banking_operations_valid) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_valid_canceled(banking_operations_valid: list[dict]):
    """Проверяет работу функции в позитивном сценарии с заданным ключом"""
    assert filter_by_state(banking_operations_valid, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_no_state(banking_operations_no_state: list[dict]):
    """Проверяет падение функции при отсутствии необходимого ключа"""
    with pytest.raises(KeyError):
        filter_by_state(banking_operations_no_state)


def test_filter_by_state_empty(banking_operations_empty: list[dict]):
    """Проверяет работу функции с пустым списком"""
    assert filter_by_state(banking_operations_empty) == []


def test_sort_by_date(banking_operations_valid: list[dict]):
    """Проверяет работу функции сортировки даты по убыванию"""
    assert sort_by_date(banking_operations_valid) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_ascending(banking_operations_valid: list[dict]):
    """Проверяет работу функции сортировки по возрастанию"""
    assert sort_by_date(banking_operations_valid, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_equally_date(banking_operations_equally_date: list[dict]):
    """Проверяет работу функции сортировки при одинаковых датах"""
    assert sort_by_date(banking_operations_equally_date, True) == [
        {"id": 111, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 222, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 333, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 444, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_sort_by_date_invalid_type(banking_operations_bad_date_type_int: list[dict]):
    """Проверяет, что функция падает с TypeError, если тип даты некорректен (число)."""
    with pytest.raises(TypeError):
        sort_by_date(banking_operations_bad_date_type_int)


def test_sort_by_date_invalid_type_2(banking_operations_bad_date_type_none: list[dict]):
    """Проверяет, что функция падает с TypeError, если тип даты некорректен (None)."""
    with pytest.raises(TypeError):
        sort_by_date(banking_operations_bad_date_type_none)


def test_sort_by_date_no_iso(banking_operations_no_iso: list[dict]):
    """Проверяет, что функция отсортирует список с датами не в ISO 8601 формате как строку"""
    assert sort_by_date(banking_operations_no_iso) == [
        {"id": 4, "date": "05.05.2026"},
        {"id": 3, "date": "04.04.1917"},
        {"id": 2, "date": "03.03.2005"},
        {"id": 1, "date": "02.02.1993"},
    ]
