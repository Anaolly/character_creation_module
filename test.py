from math import sqrt


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        root = 0
    root = calculate_square_root(your_number)
    return ('Мы вычислили квадратный корень из введённого '
            f'вами числа. Это будет: {root}')


message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)
print(calc(25.5))
