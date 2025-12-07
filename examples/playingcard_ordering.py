#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass, field

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♠ ♥ ♦ ♣'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

queen_of_hearts = PlayingCard('Q', '♥')
ace_of_spades = PlayingCard('A', '♠')
print(ace_of_spades > queen_of_hearts) 