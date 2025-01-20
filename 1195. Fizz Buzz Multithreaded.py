from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.cv = Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        with self.cv:
            while self.current <= self.n:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    break
                printFizz()
                self.current += 1
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            while self.current <= self.n:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    break
                printBuzz()
                self.current += 1
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            while self.current <= self.n:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    break
                printFizzBuzz()
                self.current += 1
                self.cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cv:
            while self.current <= self.n:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    break
                printNumber(self.current)
                self.current += 1
                self.cv.notify_all()
