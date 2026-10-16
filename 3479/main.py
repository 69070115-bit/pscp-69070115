"""Name of Card"""
card = input().strip().upper()

ranks = {
    'A': 'Ace',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King'
}

suits = {
    'D': 'Diamonds',
    'H': 'Hearts',
    'S': 'Spades',
    'C': 'Clubs'
}

rank = card[:-1]
suit = card[-1]

rank_name = ranks.get(rank, rank)
suit_name = suits[suit]

print(f"{rank_name} of {suit_name}")
