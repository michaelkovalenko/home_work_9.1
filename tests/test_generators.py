import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


def test_transaction_descriptions_valid_input(transactions_valid_input):
    """Проверка работы функции с корректными данными"""
    it = transaction_descriptions(transactions_valid_input)
    assert next(it) == "Перевод организации"
    assert next(it) == "Перевод со счета на счет"
    assert next(it) == "Перевод со счета на счет"
    assert next(it) == "Перевод с карты на карту"
    assert next(it) == "Перевод организации"

    with pytest.raises(StopIteration):
        next(it)


def test_transaction_descriptions_empty_transaction():
    """Проверка работы функции с пустым списком транзакций"""
    it = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(it)


def test_transaction_descriptions_invalid_input(transactions_invalid_input_for_description):
    """Проверка работы функции с некорректными типами данных"""
    it = transaction_descriptions(transactions_invalid_input_for_description)
    assert next(it) is None
    assert next(it) is None
    assert next(it) is None
    assert next(it) is None
    assert next(it) is None

    with pytest.raises(StopIteration):
        next(it)


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            4,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
            ],
        ),
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        (
            1234567890123456,
            1234567890123459,
            [
                "1234 5678 9012 3456",
                "1234 5678 9012 3457",
                "1234 5678 9012 3458",
                "1234 5678 9012 3459",
            ],
        ),
        (22, 22, ["0000 0000 0000 0022"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_valid_input(start, stop, expected):
    """Проверяет позитивные сценарии работы функции с помощью параметризации."""
    it = card_number_generator(start, stop)
    for number in expected:
        assert next(it) == number
    with pytest.raises(StopIteration):
        next(it)


@pytest.mark.parametrize(
    "start, stop, text_error",
    [
        (0, 4, "Неверно задан диапазон номера."),
        (4, 3, "Неверно задан диапазон номера."),
        (1, 10000000000000000, "Неверно задан диапазон номера."),
    ],
)
def test_card_number_generator_invalid_input_value(start, stop, text_error):
    """Проверяет негативные сценарии работы функции - с некорректными значениями, с помощью параметризации."""
    it = card_number_generator(start, stop)
    with pytest.raises(ValueError) as value_error:
        next(it)
    assert str(value_error.value) == text_error


@pytest.mark.parametrize(
    "start, stop",
    [
        ("0", "5"),
        (None, 5),
        (1, None),
        ([1, 2], 5),
        (1, {"stop": 9999}),
        (1.5, 5),
    ],
)
def test_card_number_generator_invalid_input_type(start, stop):
    """Проверяет негативные сценарии работы функции - с неверными типами входных данных, с помощью параметризации"""
    it = card_number_generator(start, stop)  # noqa
    with pytest.raises(TypeError) as type_error:
        next(it)
    assert str(type_error.value) == "Аргументы start и end должны быть целыми числами (int)!"
