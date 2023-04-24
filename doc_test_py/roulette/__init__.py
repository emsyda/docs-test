import random

def play_russian_roulette():
    """Play Russian roulette."""
    if random.randint(1, 6) == 6:
        print("You died!")
