from tqdm import trange
from colorama import Fore
import time

class Pomo():
    def __init__(self, study_timer, break_timer):
        self.study_timer = study_timer * 60
        self.break_timer = break_timer * 60


    def PomoTimer(self) -> None:
        for i in trange(self.study_timer, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
            time.sleep(1)
        print("----------------------------------Break Time----------------------------------")
        for i in trange(self.break_timer, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
            time.sleep(1)
        x = input("Restart?[y/n] ")
        if x == 'y':
            self.PomoTimer()
        else:
            return

study_time = int(input("how long do ya wanna study for? "))
break_time = int(input("how long do ya wanna take a break for? "))

Pomo(study_time, break_time).PomoTimer()
