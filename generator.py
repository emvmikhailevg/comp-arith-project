import random


def pseudo_random_generator(seed, low, high, size):
    random.seed(seed)
    return [random.randint(low, high) for _ in range(size)]


def generate_constants(seed):
    random.seed(seed)
    return {
        'a': random.randint(1, 10),
        'b': random.randint(1, 10),
        'c': random.randint(1, 10)
    }
