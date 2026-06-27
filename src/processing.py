def filter_by_state(banking_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение (по умолч. 'EXECUTED')"""
    return [b for b in banking_operations if b["state"] == state]

