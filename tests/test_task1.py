#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from order_tracking import Order, OrderContainer


class TestOrder:
    def test_order_creation(self):
        order = Order(order_id=1, client="Test Client", amount=1000.50)
        assert order.order_id == 1
        assert order.client == "Test Client"
        assert order.amount == 1000.50

    def test_order_repr(self):
        order = Order(order_id=2, client="Another", amount=500.75)
        repr_str = repr(order)
        assert "Order" in repr_str
        assert "order_id=2" in repr_str
        assert "client='Another'" in repr_str
        assert "amount=500.75" in repr_str


class TestOrderContainer:
    @pytest.fixture
    def container(self):
        return OrderContainer()

    @pytest.fixture
    def populated_container(self):
        container = OrderContainer()
        container.add_order(1, "Client A", 15000.00)
        container.add_order(2, "Client B", 8000.00)
        container.add_order(3, "Client C", 12000.50)
        container.add_order(4, "Client D", 5000.00)
        container.add_order(5, "Client E", 20000.75)
        return container

    def test_empty_container(self, container):
        assert len(container.get_all_orders()) == 0
        assert container.get_orders_above_amount(1000) == []

    def test_add_order(self, container):
        container.add_order(100, "Test", 5000.00)
        orders = container.get_all_orders()
        assert len(orders) == 1
        assert orders[0].order_id == 100
        assert orders[0].client == "Test"
        assert orders[0].amount == 5000.00

    def test_get_all_orders_returns_copy(self, container):
        container.add_order(1, "Test", 1000.00)
        orders1 = container.get_all_orders()
        orders2 = container.get_all_orders()
        assert orders1 == orders2
        assert orders1 is not orders2

    def test_get_orders_above_amount_empty(self, container):
        result = container.get_orders_above_amount(1000)
        assert result == []

    def test_get_orders_above_amount_none(self, populated_container):
        result = populated_container.get_orders_above_amount(50000.00)
        assert result == []

    def test_get_orders_above_amount_all(self, populated_container):
        result = populated_container.get_orders_above_amount(0.00)
        assert len(result) == 5

    def test_get_orders_above_amount_some(self, populated_container):
        result = populated_container.get_orders_above_amount(10000.00)
        assert len(result) == 3
        order_ids = {order.order_id for order in result}
        assert order_ids == {1, 3, 5}
        for order in result:
            assert order.amount > 10000.00

    def test_get_orders_above_amount_exact_boundary(self, populated_container):
        result = populated_container.get_orders_above_amount(12000.00)
        order_ids = {order.order_id for order in result}
        assert 3 in order_ids
        result2 = populated_container.get_orders_above_amount(12000.50)
        order_ids2 = {order.order_id for order in result2}
        assert 3 not in order_ids2


def test_integration():
    container = OrderContainer()
    container.add_order(101, "Иванов", 15000.00)
    container.add_order(102, "Петров", 7500.00)
    container.add_order(103, "Сидоров", 22000.00)
    all_orders = container.get_all_orders()
    assert len(all_orders) == 3
    high_value = container.get_orders_above_amount(10000.00)
    assert len(high_value) == 2
    very_high_value = container.get_orders_above_amount(20000.00)
    assert len(very_high_value) == 1
    assert very_high_value[0].order_id == 103
    container.add_order(104, "Кузнецов", 9500.00)
    medium_value = container.get_orders_above_amount(8000.00)
    assert len(medium_value) == 3
