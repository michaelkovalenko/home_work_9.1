import pytest

from src.widget import mask_account_card


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
    assert mask_account_card(number_input) == expected


@pytest.mark.parametrize("invalid_input, error_message", [
    ("Maestro", "Отсутствует номер карты или счёта"),
    ("Счет", "Отсутствует номер карты или счёта"),
])
def test_mask_account_card_empty_input(invalid_input, error_message):
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("invalid_input, error_message", [
    ("Maestro 15968378687051", "Неверное количество символов"),
    ("Visa 1596837868705192123213", "Неверное количество символов"),
    ("Master Card 159683786v705193", "Некорректный формат номера. Допускаются только цифры!"),
    ("Master Card c159683786270519", "Неверное количество символов"),
])
def test_mask_account_card_invalid_input_card(invalid_input, error_message):
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("invalid_input, error_message", [
    ("Счет 3538303347444789556", "Неверное количество символов"),
    ("Счет 35383033474447231389556", "Неверное количество символов"),
    ("Счет 6468647367889477v589", "Некорректный формат номера. Допускаются только цифры!"),
])
def test_mask_account_card_invalid_input_account(invalid_input, error_message):
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(invalid_input)