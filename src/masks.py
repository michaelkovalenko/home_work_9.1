def get_mask_card_number(card_number: str | int) -> str:
    """Принимает номер карты и возвращает её маску"""
    card_number_str_clear = "".join(str(card_number).split())
    if not card_number_str_clear:
        raise ValueError("Номер не должен быть пустым или содержать только пробелы!")
    if not card_number_str_clear.isdigit():
        raise ValueError("Некорректный формат номера. Допускаются только цифры!")
    if len(card_number_str_clear) != 16:
        raise ValueError("Неверная длина номера. Должно быть 16 цифр")
    mask = card_number_str_clear[:4] + " " + card_number_str_clear[4:6] + "** **** " + card_number_str_clear[12:]
    return mask


def get_mask_account(account_number: str | int) -> str:
    """Принимает номер счёта и возвращает его маску"""
    account_number_str_clear = "".join(str(account_number).split())
    if not account_number_str_clear:
        raise ValueError("Номер не должен быть пустым или содержать только пробелы!")
    if not account_number_str_clear.isdigit():
        raise ValueError("Некорректный формат номера. Допускаются только цифры!")
    if len(account_number_str_clear) != 20:
        raise ValueError("Неверная длина номера. Должно быть 20 цифр")
    mask = "**" + account_number_str_clear[-4:]
    return mask
