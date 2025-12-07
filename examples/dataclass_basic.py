#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)  
print(queen_of_hearts)      
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))  