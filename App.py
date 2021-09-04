from tqdm import trange

from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget

from colorama import Fore

import time
from rich.panel import Panel

class Timer(Widget):
    mouse_over: Reactive[bool] = Reactive(False)
    time = int(input("How long do ya wanna study for? ")) * 60


    def render(self) -> Panel:
    
        def PomoTimer(self):
            for i in trange(self.time, bar_format = "{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
                time.sleep(1)
                x = input("Restart? [y/n] ")
                if x == 'y':
                    self.PomoTimer()
                else:
                    return
        
        return Panel(self.PomoTimer())

class Pomo(App):
    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")
        await self.view.dock(Timer(), edge="top")

Pomo.run(log="textual.log")
        


   # def __init__(self, timer):
   #     self.timer = timer * 60

   # def PomoTimer(self) -> None:
   #     for i in trange(self.timer, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
   #         time.sleep(1)
   #     x = input("Restart?[y/n] ")
   #     if x == 'y':
   #         self.PomoTimer()
   #     else:
   #         return 
    


