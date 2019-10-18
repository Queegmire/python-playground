import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Before func called
        val = func(*args, **kwargs)
        # After fun called
        return val
    return wrapper
