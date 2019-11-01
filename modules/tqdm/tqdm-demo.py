from tqdm import tqdm, trange
from time import sleep
from random import randint
import os
if os.name == 'nt':
    try:
        import colorama
        colorama.init()
    except Exception as e:
        print("*** TRIED AND FAILED TO IMPORT COLORAMA ***")


print("Shows progress through alphabet with custom description")
pbar = tqdm("abcdefghijklmnopqrstuvwxyz")
for char in pbar:
    sleep(0.25)
    pbar.set_description(f"Working on task '{char}'")
print("Done!")
print()

print("Nested progress bars (needs colorama on windows)")
for i in trange(4, desc='1st loop'):
    for j in trange(5, desc='2nd loop'):
        for k in trange(50, desc='3rd loop', leave=False):
            sleep(0.01)
print("Done!") # overwrites part of progress bar
print()

print("Progress for 1000 tasks that each take about 1/20 of a second each")
for i in tqdm(range(1_000)):
    sleep(randint(25,75) / 1000)
print("Done!")
