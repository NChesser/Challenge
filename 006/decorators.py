from functools import wraps
from time import sleep

def uppercase(func):
    @wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

def lowercase(func):
    @wraps(func)
    def wrapper(*args):
        return func(*args).lower()
    return wrapper

def sleep_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Sleeping for 2 seconds")
        sleep(2)
        return func(*args, **kwargs)
    return wrapper

@sleep_decorator
@uppercase
def get_upper_sentence():
    return "hello world"

@sleep_decorator
@lowercase
def get_lower_sentence(text):
    return text

if __name__ == '__main__':
    print(get_upper_sentence())
    print(get_lower_sentence("HELLO WORLD"))
