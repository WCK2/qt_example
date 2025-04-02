import random
import string


def generate_random_text(min_len: int, max_len: int) -> str:
    if min_len > max_len or min_len < 0:
        raise ValueError("min_len must be less than or equal to max_len and both >= 0")

    length = random.randint(min_len, max_len)
    characters = string.ascii_letters + string.digits + " "
    return ''.join(random.choices(characters, k=length))
