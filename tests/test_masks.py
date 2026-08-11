import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_input, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        (1234567890123457, "1234 56** **** 3457"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        (" 1234 5678 9012 3456 ", "1234 56** **** 3456"),
        ("12345678 90123456 ", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number_success(card_input, expected):
    """Проверка правильности маскирования номеров карт при различных корректных форматах и типах данных."""
    assert get_mask_card_number(card_input) == expected


@pytest.mark.parametrize(
    "invalid_input, error_message",
    [
        ("", "Номер не должен быть пустым или содержать только пробелы!"),
        ("   ", "Номер не должен быть пустым или содержать только пробелы!"),
        ("123456789ноль123456", "Некорректный формат номера. Допускаются только цифры!"),
        (1234567890, "Неверная длина номера. Должно быть 16 цифр"),
        ("12345678901234567890", "Неверная длина номера. Должно быть 16 цифр"),
    ],
)
def test_get_mask_card_number_error(invalid_input, error_message):
    """Проверка вызова ValueError с ожидаемым сообщением при передаче некорректных номеров карт."""
    with pytest.raises(ValueError, match=error_message):
        get_mask_card_number(invalid_input)


@pytest.mark.parametrize(
    "account_input, expected",
    [
        ("12345678901234567890", "**7890"),
        (12345678901234567891, "**7891"),
        ("1234 5678 9012 3456 7890", "**7890"),
        (" 12345678901234567890 ", "**7890"),
        ("1234567890 1234567890 ", "**7890"),
    ],
)
def test_get_mask_account_success(account_input, expected):
    """Проверка правильности маскирования номеров счетов при различных корректных форматах и типах данных."""
    assert get_mask_account(account_input) == expected


@pytest.mark.parametrize(
    "invalid_input, error_message",
    [
        ("", "Номер не должен быть пустым или содержать только пробелы!"),
        ("   ", "Номер не должен быть пустым или содержать только пробелы!"),
        ("1234пять67890один234567890", "Некорректный формат номера. Допускаются только цифры!"),
        (1234567890123456, "Неверная длина номера. Должно быть 20 цифр"),
        (123456789012345678901234, "Неверная длина номера. Должно быть 20 цифр"),
    ],
)
def test_get_mask_account_error(invalid_input, error_message):
    """Проверка вызова ValueError с ожидаемым сообщением при передаче некорректных номеров счетов."""
    with pytest.raises(ValueError, match=error_message):
        get_mask_account(invalid_input)
