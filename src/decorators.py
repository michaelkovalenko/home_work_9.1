from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: str | None = None) -> Callable[[F], F]:
    """Декоратор для логирования результатов выполнения функций.

    Если функция завершается успешно, записывает имя функции и статус 'ok'.
    При возникновении ошибки фиксирует её тип, текст и входные аргументы,
    после чего пробрасывает исключение дальше.

    :param filename: Имя файла для записи логов. Если не указано,
                     логи выводятся в консоль через print.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)

                my_log_ok = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{my_log_ok}\n")
                else:
                    print(my_log_ok)

                return result

            except Exception as e:
                type_error = type(e).__name__
                my_log_err = f"{func.__name__} error: {type_error}: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{my_log_err}\n")
                else:
                    print(my_log_err)
                raise

        return wrapper  # type: ignore[return-value]

    return decorator
