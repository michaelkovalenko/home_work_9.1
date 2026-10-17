from collections.abc import Generator, Iterator


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
            and (curr_2 := curr_1.get("currency"))  # noqa
            and curr_2.get("code") == currency
        ):
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str | None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по одной"""
    for transaction in transactions:
        yield value if isinstance((value := transaction.get("description")), str) else None


def card_number_generator(start: int = 0, stop: int = 9999999999999999) -> Generator[str, None, None]:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генерирует номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999. Принимает начальное и конечное значения для
    генерации диапазона номеров. По умолчанию 0000 0000 0000 0000, 9999 9999 9999 9999"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Аргументы start и end должны быть целыми числами (int)!")
    if not (1 <= start <= stop <= 9999999999999999):
        raise ValueError("Неверно задан диапазон номера.")
    for number in range(start, stop + 1):
        full_number = f"{number:016}"
        yield f"{full_number[0:4]} {full_number[4:8]} {full_number[8:12]} {full_number[12:]}"
