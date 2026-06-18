import masks

def mask_account_card(type_and_number: str) -> str:
    """Определяет тип номера, возвращает маску номера карты или счёта, в зависимости от типа номера,
     указывает на тип номера вначале возвращаемой строки: счёт или название карты"""
    words = type_and_number.split()
    if len(words[-1]) == 16:
        return f"{" ".join(words[:-1])} {masks.get_mask_card_number(words[-1])}"
    else:
        return f"{" ".join(words[:-1])} {masks.get_mask_account(words[-1])}"

