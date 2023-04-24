__author__ = 'emsyda'

from .functions import create_a_random_number_that_contains_digit
from .roulette import play_russian_roulette

def main_func():
    play_russian_roulette()
    print(create_a_random_number_that_contains_digit(3))
