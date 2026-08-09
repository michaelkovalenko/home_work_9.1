import pytest


@pytest.fixture
def banking_operations_valid() -> list[dict]:
    """Возвращает список транзакций с полным набором данных"""
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def banking_operations_no_state() -> list[dict]:
    """Возвращает список транзакций, в некоторых словарях которого отсутствует ключ 'state'"""
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def banking_operations_empty() -> list[dict]:
    """Возвращает пустой список для проверки граничных случаев"""
    return []


@pytest.fixture
def banking_operations_equally_date() -> list[dict]:
    """Возвращает список транзакций с полным набором данных"""
    return [
        {'id': 111, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 333, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 444, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 222, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
    ]


@pytest.fixture
def banking_operations_bad_date_type_int() -> list[dict]:
    """Возвращает список, где вместо строки с датой передан int."""
    return [
        {'id': 1, 'date': '2024-03-11T12:00:00'},
        {'id': 2, 'date': 2024},
    ]


@pytest.fixture
def banking_operations_bad_date_type_none() -> list[dict]:
    """Возвращает список, где вместо строки с датой передан None."""
    return [
        {'id': 1, 'date': '2024-03-11T12:00:00'},
        {'id': 2, 'date': None},
    ]


@pytest.fixture
def banking_operations_no_iso() -> list[dict]:
    """Возвращает список, где дата указана не в "ISO 8601 формате"""
    return [
        {'id': 1, 'date': '02.02.1993'},
        {'id': 2, 'date': '03.03.2005'},
        {'id': 3, 'date': '04.04.1917'},
        {'id': 4, 'date': '05.05.2026'},
    ]
