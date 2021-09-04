from tqdm import trange
from colorama import Fore
import time

class Pomo():
    def __init__(self, timer):
        self.timer = timer * 60

    def PomoTimer(self) -> None:
        for i in trange(self.timer, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
            time.sleep(1)
        x = input("Restart?[y/n] ")
        if x == 'y':
            self.PomoTimer()
        else:
            return

Pomo(int(input("How long do ya wanna study for? "))).PomoTimer()
