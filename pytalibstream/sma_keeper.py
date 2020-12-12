import pyslidingwindow


class SmaKeeper:
    def __init__(self, max_len: int):
        self.arr = pyslidingwindow.SlidingWindowFloat(max_len)
        self.sma = 0

    def add(self, value: float):
        if self.arr.length() < self.arr.max_len():
            self.arr.push(value)
            self.sma = sum(self.arr) / self.arr.length()
        else:
            remove = self.arr.get(0)
            self.arr.push(value)
            max_len = self.arr.max_len()
            self.sma = self.sma - remove / max_len + value / max_len

    def get(self):
        return self.sma
