import threading
 
class DiningPhilosophers:
    def __init__(self):
        self.choppers = [threading.Semaphore(1) for _ in range(5)]
 
    def wantsToEat(self,
                   person: int,
                   l_lold_chopper: 'Callable[[], None]',
                   r_hold_chopper: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   l_drop_chopper: 'Callable[[], None]',
                   r_drop_chopper: 'Callable[[], None]') -> None:

        self.choppers[person].acquire()
        self.choppers[(person + 1) % 5].acquire()
 
       
        r_hold_chopper()
        l_lold_chopper()
        eat()
        r_drop_chopper()
        l_drop_chopper()
 
        self.choppers[person].release()
        self.choppers[(person + 1) % 5].release()

if __name__ == "__main__":
    DiningPhilosophers()