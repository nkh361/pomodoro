from tqdm import trange
import time

class Pomo():
    def __init__(self, timer):
        self.timer = timer * 60

    def PomoTimer(self):
        for i in trange(self.timer):
            time.sleep(1)

Pomo(int(input("How long do ya wanna study for? "))).PomoTimer()
