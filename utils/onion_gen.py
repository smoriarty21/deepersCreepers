import string
import random

def string_length_generator():
    min_len = 1
    max_len = 100

    return random.randint(min_len, max_len)

def generate_url():
    digits = "abcdefghijklmnopqrstuvwxyz234567"
    url = "".join([random.choice(digits) for _ in range(16)])

    return 'http://{0}.onion/'.format(url)
