#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
from typing import Callable, Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Lazy(Generic[T]):
    # Класс для ленивой инициализации значения
    factory: Callable[[], T] = field(repr=False)
    _value: Optional[T] = field(default=None, init=False, repr=False, compare=False)

    def get(self) -> T:
        # Получение значения, инициализируя его при первом обращении
        if self._value is None:
            self._value = self.factory()
        return self._value
