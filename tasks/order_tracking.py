#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
from typing import List


@dataclass
class Order:
    # Датакласс для представления заказа
    order_id: int
    client: str
    amount: float


@dataclass
class OrderContainer:
    # Контейнер для хранения и обработки заказов
    _orders: List[Order] = field(default_factory=list, repr=False)

    def add_order(self, order_id: int, client: str, amount: float) -> None:
        # Добавление нового заказа в контейнер
        new_order = Order(order_id=order_id, client=client, amount=amount)
        self._orders.append(new_order)

    def get_orders_above_amount(self, min_amount: float) -> List[Order]:
        # Получение заказа с суммой выше заданной
        result = [order for order in self._orders if order.amount > min_amount]
        return result

    def get_all_orders(self) -> List[Order]:
        # Получение всех заказов
        return self._orders.copy()

    def display_orders(self, orders_list: List[Order] = None) -> None:
        # Вывод списка заказов
        if orders_list is None:
            orders_list = self._orders

        if not orders_list:
            print("Список заказов пуст.")
            return

        print("\n" + "=" * 60)
        print(f"{'№ заказа':<12} {'Клиент':<25} {'Сумма':<10}")
        print("=" * 60)

        for order in orders_list:
            print(f"{order.order_id:<12} {order.client:<25} {order.amount:<10.2f}")
        print("=" * 60)
