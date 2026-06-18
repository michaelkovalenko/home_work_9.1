def get_mask_card_number(card_number: str | int) -> str:
    """Принимает номер карты и возвращает её маску"""
    card_number_str = str(card_number)
    mask = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[12:]
    return mask


def get_mask_account(account_number: str | int) -> str:
    """Принимает номер счёта и возвращает его маску"""
    account_number_str = str(account_number)
    mask = "**" + account_number_str[-4:]
    return mask
