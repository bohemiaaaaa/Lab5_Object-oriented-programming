#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

card = PlayingCard('A', '♥')
print(str(card))