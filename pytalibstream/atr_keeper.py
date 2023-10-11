import pyslidingwindow


class AtrKeeper:
    def __init__(self, max_len: int, high= None, low = None, close = None, _atr = 0, data_count = 0, prev_tr = []):
        if max_len < 2:
            raise Exception("AtrKeeper period must be >= 2")
        self.max_len = max_len
        self.high = pyslidingwindow.SlidingWindowFloat(max_len)
        if high is not None:
            for v in high:
                self.high.push(v)
        self.low = pyslidingwindow.SlidingWindowFloat(max_len)
        if low is not None:
            for v in low:
                self.low.push(v)
        self.close = pyslidingwindow.SlidingWindowFloat(max_len)
        if close is not None:
            for v in close:
                self.close.push(v)
        self._atr = _atr
        self.data_count = data_count
        self.prev_tr = prev_tr

    def __reduce__(self):
        return (self.__class__, (self.max_len, self.high.raw(),self.low.raw(),self.close.raw(),self._atr, self.data_count,self.prev_tr))

    def add(self, high: float, low: float, close: float):
        self.data_count += 1
        self.high.push(high)
        self.low.push(low)
        self.close.push(close)

        if self.data_count < self.max_len + 1:
            if self.data_count > 1:
                self.prev_tr.append(self.calc_tr())
        elif self.data_count == self.max_len + 1:
            self._atr = sum(self.prev_tr) / len(self.prev_tr)
            self._atr = (self._atr * (self.max_len - 1) + self.calc_tr()) / self.max_len
        else:
            self._atr = (self._atr * (self.max_len - 1) + self.calc_tr()) / self.max_len

    @staticmethod
    def get_tr(high: float, low: float, prev_close: float):
        return max(high - low, abs(high - prev_close), abs(low - prev_close))

    def calc_tr(self):
        close = self.close.get(-2) if self.close.length() > 1 else 0
        return self.get_tr(self.high.last(), self.low.last(), close)

    @property
    def atr(self):
        return self._atr
    
    def get(self):
        return self._atr
