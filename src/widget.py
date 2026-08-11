from datetime import datetime

from src import masks


def mask_account_card(type_and_number: str) -> str:
    """Определяет тип номера, возвращает маску номера карты или счёта, в зависимости от типа номера,
    указывает на тип номера вначале возвращаемой строки: счёт или название карты"""
    if not type_and_number.strip():
        raise ValueError("Номер не должен быть пустым или содержать только пробелы!")

    found_index = None
    for i, char in enumerate(type_and_number):
        if char.isdigit():
            found_index = i
            break
    else:
        raise ValueError("Отсутствует номер карты или счёта")

    name_part = type_and_number[:found_index]
    number_part = type_and_number[found_index:]
    clean_number = "".join(number_part.split())

    if len(clean_number) == 16:
        display_name = name_part.strip() if name_part.strip() else "Карта"
        return display_name + " " + masks.get_mask_card_number(number_part)
    elif len(clean_number) == 20:
        return "Счет " + masks.get_mask_account(number_part)
    else:
        raise ValueError("Неверное количество символов")


def get_date(date_iso: str) -> str:
    """Принимает на вход строку с датой в формате ISO 8601, например '2024-03-11T02:26:18.671407' и возвращает строку с
    датой в формате 'ДД.ММ.ГГГГ'"""
    date_obj = datetime.fromisoformat(date_iso)
    new_date = date_obj.strftime("%d.%m.%Y")
    return new_date
