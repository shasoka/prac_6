"""
Тесты для функции is_full_connected модуля full.

Шенберг Аркадий Алексеевич. КИ21-17/1Б. Практическая работа 6. Вариант 11.

Функции:
---------
test_is_full_connected:
    Тест на полносвязность сети.

test_si_not_full_connected:
    Тест на неполносвязность сети. Неполный ввод.

test_is_not_full_odd:
    Параметризованный тест на неполносвязность сети.
"""

import pytest
from package.full import is_full_connected


def test_is_full_connected():
    """
    Тест на полносвязность сети.
    """

    assert is_full_connected(5, 10, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2),
                                     (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])


def test_is_not_full_connected():
    """
    Тест на неполносвязность сети. Неполный ввод.
    """

    assert not is_full_connected(5, 10, [(0, 1), (0, 2), (0, 3), (0, 4),
                                         (1, 2), (1, 3), (1, 4), (2, 3),
                                         (2, 4)])


@pytest.mark.parametrize("test_input, expected",
                         [((5, 100, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]), False),
                          ((5, 10, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 100)]), False),
                          ((5, 10, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 1)]), False),
                          ((50, 10, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]), False)])
def test_is_not_full_odd(test_input, expected):
    """
    Параметризованный тест на неполносвязность сети.
    1) Полный ввод, неверное число связей.
    2) Полный ввод, некорректная связь.
    3) Полный ввод, лишняя связь.
    4) Полный ввод, неверное число ребер.
    """

    assert is_full_connected(*test_input) is expected
