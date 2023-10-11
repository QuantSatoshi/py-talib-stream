import pyslidingwindow

from .sma_keeper import SmaKeeper


class StdKeeper:
    def __init__(self, max_len: int, std = 0.0, square_sum = 0.0, sma_values = None, window_values = None):
        self.arr = pyslidingwindow.SlidingWindowFloat(max_len)
        if window_values is not None:
            for v in window_values:
                self.arr.push(v)

        self.sma_keeper = SmaKeeper(max_len)
        if sma_values is not None:
            for v in sma_values:
                self.sma_keeper.arr.push(v)
                
        self.std = std
        self.square_sum = square_sum

    def __reduce__(self):
        return (self.__class__, (self.arr.max_len(), self.std, self.square_sum, self.sma_keeper.arr.raw(), self.arr.raw()))
    
    def add(self, value: float):
        self.sma_keeper.add(value)

        if self.arr.length() < self.arr.max_len():
            self.arr.push(value)
            sma = sum(self.arr) / self.arr.length()
            variance = sum([((x - sma) ** 2) for x in self.arr]) / self.arr.length()
            self.std = variance ** 0.5
            self.square_sum += value * value
        else:
            remove = self.arr.get(0)
            self.arr.push(value)
            sma = self.sma_keeper.get()
            self.square_sum = self.square_sum + value * value - remove * remove

            middle_val_sum = sma * 2 * sma
            std_square = (
                self.square_sum / self.arr.max_len() - middle_val_sum + sma * sma
            )
            self.std = std_square ** 0.5

    def get(self):
        return float(self.std)

    def get_sma(self):
        return self.sma_keeper.get()
