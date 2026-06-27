def filter_by_state(banking_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтр банковских операций по завершённости.

    Принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение (по умолч. 'EXECUTED').
    """
    return [b for b in banking_operations if b["state"] == state]


def sort_by_date(banking_operations: list[dict], sort_order: bool = True) -> list[dict]:
    """Сортировка банковских операций по дате.

    Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате.
    """
    return sorted(banking_operations, key=lambda k: k["date"], reverse=sort_order)
