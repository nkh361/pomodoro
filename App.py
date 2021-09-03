from tqdm import trange
import time

class Pomo():
    def __init__(self, timer):
        self.timer = timer * 60

    def PomoTimer(self) -> None:
        for i in trange(self.timer):
            time.sleep(1)
        x = input("Restart?[y/n] ")
        if x == 'y':
            self.PomoTimer()
        else:
            return 
    

Pomo(int(input("How long do ya wanna study for? "))).PomoTimer()
