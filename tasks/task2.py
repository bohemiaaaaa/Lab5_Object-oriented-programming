#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from lazy_package.lazy_init import Lazy


def main() -> None:
    print("=" * 60)
    print("Демонстрация Lazy(Generic[T])")
    print("=" * 60)

    # Пример 1: Базовая демонстрация
    print("\n1. Ленивая строка:")
    lazy_string = Lazy[str](factory=lambda: "Рябинин" + " Егор")
    print("   Объект создан, factory ещё не вызвана")
    print(f"   Первый вызов get(): {lazy_string.get()}")
    print(f"   Второй вызов get(): {lazy_string.get()} (кэшировано)")

    # Пример 2: С подсчётом вызовов factory
    print("\n2. Проверка однократного вызова factory:")
    call_count = 0

    def counting_factory() -> str:
        nonlocal call_count
        call_count += 1
        return f"factory вызвана {call_count} раз"

    lazy_counter = Lazy[str](factory=counting_factory)
    result1 = lazy_counter.get()
    result2 = lazy_counter.get()
    print(f"   Результат 1: {result1}")
    print(f"   Результат 2: {result2}")
    print(f"   call_count = {call_count} (factory вызвана 1 раз)")

    # Пример 3: С числом (вычисление в factory)
    print("\n3. Ленивое число с вычислением в factory:")
    lazy_number = Lazy[int](factory=lambda: 10 + 32)
    print(f"   Результат get(): {lazy_number.get()}")


if __name__ == "__main__":
    main()
