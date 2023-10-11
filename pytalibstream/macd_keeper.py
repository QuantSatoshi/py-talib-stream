from pytalibstream.ema_keeper import *


class MacdKeeper:
    def __init__(self, fast_period: int, slow_period: int, signal_period: int, slow_ema = 0, fast_ema =0, signal_ema = 0, macd = 0, data_count = 0):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

        if self.slow_period < self.fast_period:
            raise Exception(
                "slowPeriod {} cannot be smaller than fastPeriod {}".format(
                    self.slow_period, self.fast_period
                )
            )
        if self.fast_period < self.signal_period:
            raise Exception(
                "fastPeriod {} cannot be smaller than signalPeriod {}".format(
                    self.fast_period, self.signal_period
                )
            )

        self.slow_ema_keeper = EmaKeeper(self.slow_period, slow_ema)
        self.fast_ema_keeper = EmaKeeper(self.fast_period, fast_ema)
        self.signal_ema_keeper = EmaKeeper(self.signal_period, signal_ema)
        self._macd = macd
        self.data_count = data_count

    def __reduce__(self):
        return (self.__class__, (self.fast_period, self.slow_period, self.signal_period, self.slow_ema_keeper.get(), self.fast_ema_keeper.get(), self.signal_ema_keeper.get(), self._macd, self.data_count))

    def add(self, value: float):
        self.data_count += 1
        self.slow_ema_keeper.add(value)

        if self.data_count > self.slow_period - self.fast_period:
            self.fast_ema_keeper.add(value)

        if self.data_count >= self.slow_period:
            self._macd = self.fast_ema_keeper.ema - self.slow_ema_keeper.ema
            self.signal_ema_keeper.add(self._macd)

    def get(self):
        macd = (
            self._macd
            if self.data_count >= self.slow_period + self.signal_period - 1
            else 0
        )
        return {
            "macd": macd,
            "macdSignal": self.signal_ema_keeper.ema,
            "histogram": macd - self.signal_ema_keeper.ema,
        }
