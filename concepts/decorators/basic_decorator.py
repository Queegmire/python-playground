# Basic decorator pattern
def decorator_func(original_func):
    print('#' * 10, 'This runs once for each decorated function')
    print(f'Decorating "{original_func.__name__}"')
    print(f'Have access to "{original_func.__name__}"')

    def wrapper(*args, **kwargs):
        print(f'In wrapper - before calling "{original_func.__name__}"')
        original_val = original_func(*args, **kwargs)
        print(f'In wrapper - after calling "{original_func.__name__}"')
        return original_val
    print(f'Now have access to "{wrapper.__name__}"')
    print(f'"{original_func.__name__}" decorated with "{wrapper.__name__}"')
    print()
    return wrapper


def my_function(stuff, more_stuff='whatever'):
    print('In the original function doing cool stuff')
    print(f'stuff = {stuff}, more_stuff = {more_stuff}')
    return stuff + more_stuff


@decorator_func
def my_decorated_function(stuff, more_stuff='whatever'):
    print('In the original function doing cool stuff')
    print(f'stuff = {stuff}, more_stuff = {more_stuff}')
    return stuff + more_stuff


print("#" * 10, 'calling undecorated function')
my_function('undecorated', more_stuff='with more_stuff')
print()
print("#" * 10, 'calling decorated function')
my_decorated_function('decorated', more_stuff='with more_stuff')
print()
