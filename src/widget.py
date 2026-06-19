import masks

def mask_account_card(type_and_number: str) -> str:
    """Определяет тип номера, возвращает маску номера карты или счёта, в зависимости от типа номера,
    указывает на тип номера вначале возвращаемой строки: счёт или название карты"""
    words = type_and_number.split()
    if not words:
        return "Пустой ввод"
    elif len(words[-1]) == 16:
        if len(words) >= 2:
            return f"{" ".join(words[:-1])} {masks.get_mask_card_number(words[-1])}"
        else:
            return "Некорректный ввод. Введите название карты"
    elif len(words[-1]) == 20:
        if len(words) > 2:
            return "Введено слишком длинное значение. Оставьте только слово 'Счёт' и его номер"
        elif len(words) == 2:
            return f"{" ".join(words[:-1])} {masks.get_mask_account(words[-1])}"
        else:
            return "Счет " + masks.get_mask_account(words[-1])
    else:
        return "Некорректное количество символов в номере"


def get_date(date: str) -> str:
    """Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407' и возвращает строку с датой
    в формате 'ДД.ММ.ГГГГ'"""
    new_date = date[8:10] + "." + date[5:7] + "." + date[0:4]
    return new_date
