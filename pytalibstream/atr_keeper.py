from typing import Optional
import pyslidingwindow


class AtrKeeper:
    def __init__(self, max_len: Optional[int] = 10):
        if max_len < 2:
            raise Exception(
                "AtrKeeper period must be >= 2")

        self.high = pyslidingwindow.SlidingWindowFloat(max_len)
        self.low = pyslidingwindow.SlidingWindowFloat(max_len)
        self.close = pyslidingwindow.SlidingWindowFloat(max_len)
        self._atr = 0
        self.data_count = 0
        self.max_len = max_len
        self.prev_tr = []

    def add(self, high: float, low: float, close: float):
        self.data_count += 1
        self.high.push(high)
        self.low.push(low)
        self.close.push(close)

        if self.max_len + 1 > self.data_count > 1:
            self.prev_tr.append(self.tr)
        elif self.data_count == self.max_len+1:
            self._atr = sum(self.prev_tr) / len(self.prev_tr)
            self._atr = (self._atr * (self.max_len - 1) + self.tr) / self.max_len
        else:
            self._atr = (self._atr * (self.max_len - 1) + self.tr) / self.max_len

    @staticmethod
    def get_tr(high: float, low: float, close: float):
        return max(high - low, abs(high - close), abs(low - close))

    @property
    def tr(self):
        close = self.close.get(-2) if self.close.length() > 1 else 0
        return self.get_tr(self.high.last(), self.low.last(), close)

    @property
    def atr(self):
        return self._atr
