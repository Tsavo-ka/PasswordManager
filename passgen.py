import string
from random import choice, shuffle

ASCII = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

def pass_generator():
    chars = [choice(ASCII) for _ in range(16)]
    shuffle(chars)

    return ''.join(chars)



