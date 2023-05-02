import random

def generate_secret_number():
    """
    Generates a random 4-digit number with unique digits.
    """
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return digits[:4]
