import md5
import string
import random

def scrub_url(url):
    new_url = ''
    for letter in url:
        if letter.isdigit():
            if letter > 7 or letter < 2:
                letter = random.randint(2,7)
        new_url += str(letter)
    return new_url

def string_length_generator():
    min_len = 1
    max_len = 100

    return random.randint(min_len, max_len)

def generate_noise(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_url():
    noise = generate_noise(string_length_generator())

    m = md5.new()
    m.update(noise)
    url = m.hexdigest()
    url = scrub_url(url[:len(url)/2])

    return 'http://{0}.onion/'.format(url)
