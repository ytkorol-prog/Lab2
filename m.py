# m.py
"""Модуль для практичної роботи №2 (ООПСУ).

Містить 3 функції для завдань 1–3:
1) розгалуження (if2)
2) геометрична область (цикл for)
3) ряд на збіжність/розбіжність (цикл while)

Автор: Король Ярослав Тарасович, гр. 322
"""

from __future__ import annotations


def task_if2() -> None:
    """Завдання 1 (if2).
    Дано ціле число x. Якщо x > 0 — відняти 8, інакше — додати 6.
    """
    try:
        x = int(input("Введіть ціле число x: "))
    except ValueError:
        print("Помилка: потрібно ввести ЦІЛЕ число!")
        return

    if x > 0:
        x -= 8
    else:
        x += 6

    print("Результат:", x)


def task_geom() -> None:
    """Завдання 2 (геометрична область), варіант 2.

    Параметри прямокутника: 0<=y<=a, 0<=x<=b
    a=1, b=3
    Коло: центр (b/2, a/2), r=a/2

    Темно-оливкова область = (ліва половина кола) U (права частина прямокутника поза колом).
    """
    a = 1.0
    b = 3.0

    try:
        n = int(input("Введіть кількість точок n: "))
        if n <= 0:
            print("Помилка: n має бути додатним!")
            return
    except ValueError:
        print("Помилка: потрібно ввести ЦІЛЕ число n!")
        return

    count = 0
    r2 = (a / 2) ** 2
    cx, cy = b / 2, a / 2

    for i in range(1, n + 1):
        try:
            x = float(input(f"x{i} = "))
            y = float(input(f"y{i} = "))
        except ValueError:
            print("Помилка: координати мають бути ДІЙСНИМИ числами!")
            return

        circle = (x - cx) ** 2 + (y - cy) ** 2

        in_left_half_circle = (circle <= r2) and (x <= cx)
        in_right_rectangle_outside_circle = (circle >= r2) and (cx <= x <= b) and (0 <= y <= a)

        if in_left_half_circle or in_right_rectangle_outside_circle:
            count += 1

    print("Кількість точок у темно-оливковій області:", count)


def task_series() -> None:
    """Завдання 3 (ряд на збіжність/розбіжність), варіант 2.

    Умова зупинки:
      |u_n| < E  -> збігається
      |u_n| > G  -> розбігається
    """
    try:
        e = float(input("Введіть E (наприклад 1e-8): "))
        g = float(input("Введіть G (наприклад 1e4): "))
        if e <= 0 or g <= 0:
            print("Помилка: E та G мають бути додатними!")
            return
    except ValueError:
        print("Помилка: потрібно ввести ДІЙСНІ числа E та G!")
        return

    n = 1
    u = 0.5  # u1 = 1/2
    s = u

    max_iter = 200000
    while True:
        if abs(u) < e:
            print(f"Ряд збігається (|u_n| < E). n={n}, S≈{s}")
            return
        if abs(u) > g:
            print(f"Ряд розбігається (|u_n| > G). n={n}, S≈{s}")
            return
        if n >= max_iter:
            print(f"Досягнуто max_iter={max_iter}. n={n}, |u|={abs(u)}, S≈{s}")
            return

        n += 1
        u = u * (4 * n - 3) / ((4 * n - 2) * (4 * n - 4))
        s += u
