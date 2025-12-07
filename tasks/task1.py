#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from order_tracking import OrderContainer


def main() -> None:
    container = OrderContainer()

    container.add_order(1001, "Иванов А.А.", 12500.50)
    container.add_order(1002, "Петров Б.Б.", 8500.00)
    container.add_order(1003, "Сидоров В.В.", 21000.75)
    container.add_order(1004, "Кузнецов Г.Г.", 5500.25)
    container.add_order(1005, "Смирнов Д.Д.", 18000.00)

    print("=" * 60)
    print("Все заказы:")
    container.display_orders()

    min_amount = 10000.00
    print(f"\nЗаказы с суммой выше {min_amount:.2f}:")
    filtered_orders = container.get_orders_above_amount(min_amount)
    container.display_orders(filtered_orders)

    min_amount2 = 15000.00
    print(f"\nЗаказы с суммой выше {min_amount2:.2f}:")
    filtered_orders2 = container.get_orders_above_amount(min_amount2)
    container.display_orders(filtered_orders2)


if __name__ == "__main__":
    main()
