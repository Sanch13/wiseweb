import doctest
from functools import wraps

################
# Lst is Lst #
################

CONTROL_LST = [1, 7, 2, 7, 3, 7, 4, 7]


def lis_is_lst(a: list, b: list, dlt: int = 1) -> None:
    """
    Реализовать тело функции что бы c == CONTROL_LST
    >>> lis_is_lst([7, 7, 7, 7], [4, 2, 1, 3])
    True
    >>> lis_is_lst(["1234"], [7, 7, 7])
    True
    >>> lis_is_lst([1, 4, 3, 7, 2], [])
    True
    """
    c = a + b
    for i, el in enumerate(c):  # проходим по списку с
        if type(el) != int:     # если элемент не int
            c.extend(map(int, c.pop(i)))  # Удаляем его и расширяем в конец списка приводя каждый
            # элемент последовательности в int
    c = sorted(c)[:4]  # сортируем и берем срез [1, 2, 3, 4]
    for i in range(1, 8, 2):
        c.insert(i, 7)  # вставляем 7 в нужные позиции
    print(c == CONTROL_LST * dlt)


#############
# The Magic #
#############


def decorate_for_you(func):
    digits = {1: "Low Result: ", 2: "Result: ", 3: "Great Result: "}

    @wraps(func)
    def wrapper(some_int):
        return f"{digits.get(len(str(some_int)))}{func(some_int)}"

    return wrapper


@decorate_for_you
def decorate_me(some_int):
    """
    Написать декоротор для функции(но не изменять саму функцию) что бы при выполнении следующего кода вывод был следущим:
    >>> decorate_me(25)
    'Result: 50'
    >>> decorate_me(196)
    'Great Result: 392'
    >>> decorate_me(2)
    'Low Result: 4'
    """
    return some_int * 2


def magic_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@magic_decorator
def magic(stall=[]):
    """
    Написать декоротор для функции(но не изменять саму функцию) что бы при выполнении следующего кода вывод был следущим:
    >>> magic()
    ???		#  <--- Мы ожидаем знаки вопроса??? Странно как то. В общем тут я не понял.
    >>> magic()
    ???		#  <--- Мы ожидаем знаки вопроса??? Странно как то. В общем тут я не понял.
    >>> stall = []
    >>> magic(stall)
    ???		#  <--- Мы ожидаем знаки вопроса??? Странно как то. В общем тут я не понял.
    >>> stall = 45
    >>> magic(stall)
    ???		#  <--- Мы ожидаем знаки вопроса??? Странно как то. В общем тут я не понял.
    >>> stall == _
    ???		#  <--- Мы ожидаем знаки вопроса??? Странно как то. В общем тут я не понял.
    """
    unicorn = '🦄'
    if hasattr(stall, 'append') and callable(stall.append):
        stall.append(unicorn)
    elif hasattr(stall, 'add') and callable(stall.add):
        stall.add(unicorn)
    else:
        stall = unicorn

    return stall


################
# Paint It All #
################

# Заставить сработать функцию как это описано в комментарии, изменять сами классы PaintIt{Color} нельзя
from enum import Enum


class Color(Enum):
    BLACK = '⚫'
    RED = '🔴'
    GREEN = '🟢'


# Необходимо вместо этой реализации класс PaintIt написать свою
# PaintIt = type('_', (type,), {'__new__': lambda *a, **_: type.__new__(*a)})('_', (), {})
class PaintItMeta(type):
    def __new__(metacls, name, bases, attrs, **extra_kwargs):
        new_class = super().__new__(metacls, name, bases, attrs)
        key, value = *extra_kwargs.keys(), *extra_kwargs.values()
        setattr(new_class, key, value)
        return new_class

    def __call__(cls, *args, **kwargs):
        return cls.color.value


class PaintIt(metaclass=PaintItMeta, color=Color):
    ...


class PaintItBlack(PaintIt, color=Color.BLACK):
    ...


class PaintItGreen(PaintIt, color=Color.GREEN):
    ...


class PaintItRed(PaintIt, color=Color.RED):
    ...


# функцию изменять нельзя
def paint_it_all():
    """
    >>> paint_it_all()
    ⚫ 🟢 🔴
    """
    print(PaintItBlack(), PaintItGreen(), PaintItRed())


###########
# Doctest #
###########


if __name__ == "__main__":
    globs = globals()

    for test in (
            lis_is_lst, decorate_me, paint_it_all  # magic,
    ):
        # Use context managers here
        name = test.__name__
        line = "#" * (len(name) + 4)
        print(f"{line}\n# {name} #\n{line}\n")
        doctest.run_docstring_examples(test, globs, name=name)
        print()
