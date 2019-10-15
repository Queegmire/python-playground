import shutil
import sys
import time


def progressbar(char='=', goal=100):
    def decorator(func):
        def inner(*args, **kwargs):
            gen = func(*args, **kwargs)

            for progress in gen:
                max_width, _ = shutil.get_terminal_size()
                message = f'{progress*100//goal}%'
                bar_width = max_width - (len(message) + 3)
                filled = int(round(bar_width / goal * progress))
                bar = char * filled
                sys.stdout.write(f'{bar:{bar_width}} {message}\r')
                sys.stdout.flush()
            else:
                sys.stdout.write('\n')
                sys.stdout.flush()

        return inner

    return decorator


@progressbar('*', 200)
def wait(seconds):
    step = seconds / 200.0
    for i in range(1, 201):
        time.sleep(step)
        yield i


wait(12)
