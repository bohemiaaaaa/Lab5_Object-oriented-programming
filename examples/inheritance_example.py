#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str

cap = Capital('Oslo', 10.8, 59.9, 'Norway')
print(cap) 