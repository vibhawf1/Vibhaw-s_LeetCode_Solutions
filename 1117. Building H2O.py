from threading import RLock, Lock, Condition, Semaphore, Barrier


class H2O:
# class H2OCondition:
    def __init__(self):
        self.release_gate = Condition()
        self.num_h = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.release_gate:
            self.release_gate.wait_for(lambda: self.num_h < 2)
            self.num_h += 1
            releaseHydrogen()
            self.release_gate.notify_all()
            

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.release_gate:
            self.release_gate.wait_for(lambda: self.num_h == 2)
            releaseOxygen()
            self.num_h = 0
            self.release_gate.notify_all()


# class H2O:
class H2OLock:
    def __init__(self):
        self.h1_lock = Lock()
        self.h2_lock = Lock()
        self.o_lock = Lock()

        self.o_lock.acquire()
        self.h2_lock.acquire()

        self.no_h = True

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        if self.no_h:
            self.h1_lock.acquire()
        else:
            self.h2_lock.acquire()

        releaseHydrogen()

        self.no_h = not self.no_h
        if self.no_h:
            self.o_lock.release()
        else:
            self.h2_lock.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_lock.acquire()
        releaseOxygen()
        self.h1_lock.release()



# - with semaphores
# class H2O:
class H2OSemaphores:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.barrier.wait()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            releaseOxygen()
            self.barrier.wait()
    
