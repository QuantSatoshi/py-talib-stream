import pyslidingwindow


class SmaKeeper:
    def __init__(self, max_len: int, sma = 0, window_values = None):
        self.arr = pyslidingwindow.SlidingWindowFloat(max_len)
        self.sma = sma
        self.max_len = max_len
        if window_values is not None:
            for v in window_values:
                self.arr.push(v)

    def __reduce__(self):
        return (self.__class__, (self.max_len, self.sma, self.arr.raw()))

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
