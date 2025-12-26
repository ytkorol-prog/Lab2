# main.py
"""Скрипт-меню для практичної роботи №2 (ООПСУ).

Запускає завдання 1–3 з модуля m.py.
"""

import m


def main() -> None:
    while True:
        print("\n=== Практична робота №2 ===")
        print("1 - Завдання 1 (if2)")
        print("2 - Завдання 2 (геометрична область)")
        print("3 - Завдання 3 (ряд на збіжність)")
        print("0 - Вихід")

        try:
            choice = int(input("Ваш вибір: "))
        except ValueError:
            print("Помилка: введіть ціле число 0..3.")
            continue

        if choice == 0:
            print("Good bye!")
            break
        elif choice == 1:
            m.task_if2()
        elif choice == 2:
            m.task_geom()
        elif choice == 3:
            m.task_series()
        else:
            print("Невірний номер завдання! Спробуйте ще раз.")


if __name__ == "__main__":
    main()
