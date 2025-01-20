from threading import Semaphore

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Semaphore(1) for _ in range(5)]  # 5 forks as semaphores

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5

        # Use a consistent order to prevent deadlock (always acquire the lower ID fork first)
        if left_fork < right_fork:
            first_fork, second_fork = left_fork, right_fork
            pick_first, pick_second = pickLeftFork, pickRightFork
            put_first, put_second = putLeftFork, putRightFork
        else:
            first_fork, second_fork = right_fork, left_fork
            pick_first, pick_second = pickRightFork, pickLeftFork
            put_first, put_second = putRightFork, putLeftFork

        # Acquire forks
        self.forks[first_fork].acquire()
        self.forks[second_fork].acquire()

        pick_first()
        pick_second()

        eat()

        put_first()
        put_second()

        # Release forks
        self.forks[second_fork].release()
        self.forks[first_fork].release()
