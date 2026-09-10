"""card"""
card = input().upper()
card_type = card[-1]
card_value = card[:-1]
prefix = {'A' : 'ace', 'J' : 'jack', 'Q' : 'queen', 'K' : 'king'}
suffix = {'H' : 'hearts', 'D' : 'diamonds', 'C' : 'clubs', 'S' : 'spades'}
if prefix.get(card_value):
    card_value = prefix[card_value]
if suffix.get(card_type):
    card_type = suffix[card_type]
print(f"{card_value} of {card_type}")
