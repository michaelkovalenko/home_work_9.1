from collections.abc import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей с данными о транзакциях.
    :param currency: Строковый код валюты (например, 'USD', 'RUB').
    :return: Ленивый итератор, поочередно возвращающий отфильтрованные транзакции.
    """
    for transaction in transactions:
        if (
            (curr_1 := transaction.get("operationAmount"))
            and (curr_2 := curr_1.get("currency"))
            and curr_2.get("code") == currency
        ):
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str | None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по одной"""
    for transaction in transactions:
        yield value if isinstance((value := transaction.get("description")), str) else None
