import pyslidingwindow


class EmaKeeper:
    def __init__(self, max_len: int, ema = 0):
        self.arr = pyslidingwindow.SlidingWindowFloat(max_len)
        self._ema = ema
        # little hack, just push same ema value into sliding window
        if ema > 0:
            for i in range(0, max_len):
                self.arr.push(ema)

    def __reduce__(self):
        return (self.__class__, (self.arr.max_len(), self._ema))

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

    def get(self):
        return self._ema