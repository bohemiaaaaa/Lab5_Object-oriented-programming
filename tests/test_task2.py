#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from lazy_package.lazy_init import Lazy


class TestLazy:
    @pytest.fixture
    def counting_factory(self):
        self.call_count = 0

        def factory() -> str:
            self.call_count += 1
            return f"call_{self.call_count}"

        return factory

    def test_lazy_creation(self):
        lazy = Lazy[str](factory=lambda: "test")
        assert lazy._value is None

    def test_get_first_call(self):
        lazy = Lazy[str](factory=lambda: "result")
        value = lazy.get()
        assert value == "result"
        assert lazy._value == "result"

    def test_get_multiple_calls(self, counting_factory):
        lazy = Lazy[str](factory=counting_factory)

        result1 = lazy.get()
        assert result1 == "call_1"
        assert self.call_count == 1

        result2 = lazy.get()
        assert result2 == "call_1"
        assert self.call_count == 1

        result3 = lazy.get()
        assert result3 == "call_1"
        assert self.call_count == 1

    def test_different_types(self):
        lazy_str = Lazy[str](factory=lambda: "string")
        assert lazy_str.get() == "string"

        lazy_int = Lazy[int](factory=lambda: 42)
        assert lazy_int.get() == 42

        lazy_list = Lazy[list](factory=lambda: [1, 2, 3])
        assert lazy_list.get() == [1, 2, 3]

    def test_factory_with_computation(self):
        lazy = Lazy[int](factory=lambda: 10 * 5 + 2)
        assert lazy.get() == 52

    def test_none_value_initial(self):
        lazy = Lazy[str](factory=lambda: "value")
        assert lazy._value is None
        lazy.get()
        assert lazy._value is not None

    def test_repr_hides_internals(self):
        lazy = Lazy[str](factory=lambda: "hidden")
        repr_str = repr(lazy)
        assert "_value" not in repr_str
        assert "factory" not in repr_str
        assert "Lazy" in repr_str

    def test_compare_ignores_value(self):
        lazy1 = Lazy[str](factory=lambda: "first")
        lazy2 = Lazy[str](factory=lambda: "second")

        lazy1.get()
        lazy2.get()

        assert lazy1 != lazy2

    def test_same_factory_different_instances(self, counting_factory):
        lazy1 = Lazy[str](factory=counting_factory)
        lazy2 = Lazy[str](factory=counting_factory)

        lazy1.get()
        assert self.call_count == 1

        lazy2.get()
        assert self.call_count == 2

    def test_factory_returns_none(self):
        lazy = Lazy[type(None)](factory=lambda: None)
        result = lazy.get()
        assert result is None
        assert lazy._value is None


def test_lazy_integration():
    compute_count = 0

    def expensive() -> list[int]:
        nonlocal compute_count
        compute_count += 1
        return [compute_count] * 3

    lazy = Lazy[list[int]](factory=expensive)

    assert compute_count == 0

    result1 = lazy.get()
    assert result1 == [1, 1, 1]
    assert compute_count == 1

    result2 = lazy.get()
    assert result2 == [1, 1, 1]
    assert compute_count == 1

    result3 = lazy.get()
    assert result3 == [1, 1, 1]
    assert compute_count == 1
