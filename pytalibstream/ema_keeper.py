import pyslidingwindow


class EmaKeeper:
    def __init__(self, max_len: int):
        self.arr = pyslidingwindow.SlidingWindowFloat(max_len)
        self._ema = 0

    def add(self, value: float):
        if self.arr.length() < self.arr.max_len():
            self.arr.push(value)
            self._ema = sum(self.arr) / self.arr.length()
        else:
            self._ema = self.get_ema(self.arr.max_len(), value, self.ema)

        return self.ema

    @property
    def ema(self):
        return self._ema

    @staticmethod
    def get_ema(max_length: int, value: float, ema: float):
        k = 2 / (max_length + 1)
        return value * k + ema * (1 - k)
