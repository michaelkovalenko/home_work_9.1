import pytest

from src.decorators import log


@log(None)
def dummy_normal_console(a, b):
    """Заглушка для проверки логирования в консоль."""
    return a * b


@log("my_log.txt")
def dummy_normal_file(a, b):
    """Заглушка для проверки логирования в файл."""
    return a * b


@log(None)
def dummy_error_console(a):
    """Заглушка-имитация деления на ноль для проверки логирования ошибки в консоль"""
    return a / 0


@log("my_log.txt")
def dummy_error_file(a):
    """Заглушка-имитация деления на ноль для проверки логирования ошибки в файл."""
    return a / 0


@log(None)
def dummy_kwargs_error_console(*, a=3, b=0):
    """Заглушка для проверки логирования ошибки в консоль при вызове функции с именованными аргументами"""
    return a / b


@log("my_log.txt")
def dummy_kwargs_error_file(*, a=3, b=0):
    """Заглушка для проверки логирования ошибки в файл при вызове функции с именованными аргументами"""
    return a / b


@log(None)
def dummy_empty_def():
    """Заглушка для проверки логирования, когда функция возвращает None."""
    return None


def test_normal_console(capsys):
    """Проверяет вывод лога в консоль при успешном завершении работы функции."""
    dummy_normal_console(1, 2)

    captured = capsys.readouterr()

    assert captured.out == "dummy_normal_console ok\n"


def test_normal_file():
    """Проверяет запись лога в файл при успешном завершении работы функции."""
    dummy_normal_file(1, 2)
    with open("my_log.txt", "r") as f:
        assert f.readlines()[-1] == "dummy_normal_file ok\n"


def test_error_console(capsys):
    """Проверяет соответствие лога ошибки при выведении в консоль."""
    with pytest.raises(ZeroDivisionError):
        dummy_error_console(1)

    captured = capsys.readouterr()

    assert captured.out.strip() == "dummy_error_console error: ZeroDivisionError: division by zero. Inputs: (1,), {}"


def test_error_file():
    """Проверяет соответствие лога ошибки при записи в файл."""
    with pytest.raises(ZeroDivisionError):
        dummy_error_file(1)
    with open("my_log.txt", "r") as f:
        assert f.readlines()[-1].strip() == (
            "dummy_error_file error: ZeroDivisionError:" " division by zero. Inputs: (1,), {}"
        )


def test_kwargs_error_console(capsys):
    """Проверяет соответствие вывода лога ошибки в консоль при вызове функции с именованными аргументами."""
    with pytest.raises(ZeroDivisionError):
        dummy_kwargs_error_console(a=1, b=0)

    captured = capsys.readouterr()

    assert captured.out.strip() == (
        "dummy_kwargs_error_console error: ZeroDivisionError:" " division by zero. Inputs: (), {'a': 1, 'b': 0}"
    )


def test_kwargs_error_file():
    """Проверяет соответствие записи лога ошибки в файл при вызове функции с именованными аргументами."""
    with pytest.raises(ZeroDivisionError):
        dummy_kwargs_error_file(a=9, b=0)
    with open("my_log.txt", "r") as f:
        assert f.readlines()[-1].strip() == (
            "dummy_kwargs_error_file error: ZeroDivisionError:" " division by zero. Inputs: (), {'a': 9, 'b': 0}"
        )


def test_empty_def(capsys):
    """Проверяет соответствие вывода лога в консоль при вызове функции, возвращающей None."""
    assert dummy_empty_def() is None
    captured = capsys.readouterr()
    assert captured.out.strip() == "dummy_empty_def ok"


def test_log_preserves_metadata():
    """Проверяет сохранение метаданных (имени) декорируемой функции"""
    assert dummy_empty_def.__name__ == "dummy_empty_def"
