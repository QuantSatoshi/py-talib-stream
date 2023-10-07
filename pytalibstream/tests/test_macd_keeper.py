import math
import unittest

import numpy as np
import talib

from pytalibstream.macd_keeper import MacdKeeper


class TestMacdKeeper(unittest.TestCase):
    def setUp(self) -> None:
        self.macd_keeper = MacdKeeper(12, 26, 9)
        self.sample = []
        for i in range(1, 101):
            self.sample.append(float(math.log(i)))

    def test_add(self):
        self.macd_keeper.add(10)
        self.assertEqual(self.macd_keeper.slow_ema_keeper.arr.length(), 1)

    def test_macd(self):
        macd_ta = talib.MACD(
            np.array(self.sample), fastperiod=12, slowperiod=26, signalperiod=9
        )
        for i in range(0, len(self.sample)):
            self.macd_keeper.add(self.sample[i])
            # over a longer term, the macd will get close
            if i > 33:
                self.assertTrue(
                    abs(self.macd_keeper.get()["macd"] - macd_ta[0][i]) < 0.0001
                )


if __name__ == "__main__":
    unittest.main()
