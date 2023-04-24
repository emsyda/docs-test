import random

def create_a_random_number_that_contains_digit(digit):
    """
    Create a random number that contains a certain digit.
    :param digit: The digit that the number should contain.
    :return: A random number that contains the given digit.
    """
    number = random.randint(1, 1000000)
    while str(digit) not in str(number):
        number = random.randint(1, 1000000)
    return number
