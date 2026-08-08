import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("number_input, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Platinum 8990 9221 1366 5229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Platinum   89909221  13665229", "Visa Platinum 8990 92** **** 5229"),
    ("Счет 3538 3033 4744 4789 5560", "Счет **5560"),
    ("Счет   35383033474  447895560 ", "Счет **5560"),
    ("Счёт   35383033474  447895560 ", "Счет **5560"),
    ("счёт   35383033474  447895560 ", "Счет **5560"),
    ("счет   35383033474  447895560 ", "Счет **5560"),
    ("7158300734726758", "Карта 7158 30** **** 6758"),
    ("35383033474447895560", "Счет **5560"),
    (" 353830334 74447895560  ", "Счет **5560"),
    ("7158 3007 3472 6758", "Карта 7158 30** **** 6758"),
])
def test_mask_account_card_success(number_input, expected):
    """Проверка обработки функцией номеров карт и счетов, включая граничные и нестандартные случаи"""
    assert mask_account_card(number_input) == expected


@pytest.mark.parametrize("invalid_input, error_message", [
    ("Maestro", "Отсутствует номер карты или счёта"),
    ("Счет", "Отсутствует номер карты или счёта"),
])
def test_mask_account_card_empty_input(invalid_input, error_message):
    """Проверка обработки функцией ввода без номера карты или счёта"""
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("invalid_input, error_message", [
    ("Maestro 15968378687051", "Неверное количество символов"),
    ("Visa 1596837868705192123213", "Неверное количество символов"),
    ("Master Card 159683786v705193", "Некорректный формат номера. Допускаются только цифры!"),
    ("Master Card c159683786270519", "Неверное количество символов"),
])
def test_mask_account_card_invalid_input_card(invalid_input, error_message):
    """Проверка обработки функцией некорректных номеров карт"""
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("invalid_input, error_message", [
    ("Счет 3538303347444789556", "Неверное количество символов"),
    ("Счет 35383033474447231389556", "Неверное количество символов"),
    ("Счет 6468647367889477v589", "Некорректный формат номера. Допускаются только цифры!"),
])
def test_mask_account_card_invalid_input_account(invalid_input, error_message):
    """Проверка обработки функцией некорректных номеров счёта"""
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("data_input, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2026-08-08T13:39:00.123456", "08.08.2026"),
    ("2020-02-29T23:59:59.999999", "29.02.2020"),
    ("2025-01-01T00:00:00.000000", "01.01.2025"),
    ("2023-12-31T12:00:05.000500", "31.12.2023"),
    ("2024-10-05T08:05:09.003000", "05.10.2024"),
    ("2019-07-15T18:45:30.888888", "15.07.2019"),
    ("2030-05-20T07:15:42.111111", "20.05.2030"),
    ("2030-05-20", "20.05.2030"),
    ("2019-07-15T18:45:30", "15.07.2019"),
    ("2024-10-05T08:05", "05.10.2024"),
    ("2023-12-31T12", "31.12.2023"),
])
def test_get_date(data_input, expected):
    """Проверка обработки функцией разных форматов даты, включая граничные и нестандартные случаи"""
    assert get_date(data_input) == expected


@pytest.mark.parametrize("invalid_date, error_message", [
    (" ", "Invalid isoformat string"),
    ("", "Invalid isoformat string"),
    ("11.03.2024", "Invalid isoformat string"),
    ("02/03/1993", "Invalid isoformat string"),
    ("2023-12-31T1", "Invalid isoformat string"),
    ("2023-12-31T", "Invalid isoformat string"),
])
def test_get_date_invalid_and_empty_input(invalid_date, error_message):
    """Проверка обработки функцией неверного формата даты или отсутствия даты"""
    with pytest.raises(ValueError, match=error_message):
        get_date(invalid_date)


def test_get_date_missing_date_none():
    """Проверка, что функция корректно обрабатывает полное отсутствие даты (None)."""
    with pytest.raises(TypeError):
        get_date(None)  # type: ignore
