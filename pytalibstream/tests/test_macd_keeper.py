import math
import pickle
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

    def test_pickle_dump(self):
        for i in range(1, 101):
            self.sample.append(float(math.log(i)))

        # Serialize the instance to a file
   
        with open('macd_keeper.pickle', 'wb') as file:
            pickle.dump(self.macd_keeper, file)

        # Deserialize the instance from the file
        with open('macd_keeper.pickle', 'rb') as file:
            loaded_macd_keeper = pickle.load(file)
            self.assertEqual(loaded_macd_keeper.get(), self.macd_keeper.get())
            self.assertEqual(loaded_macd_keeper.slow_ema_keeper.get(), self.macd_keeper.slow_ema_keeper.get())
            self.assertEqual(loaded_macd_keeper.signal_ema_keeper.get(), self.macd_keeper.signal_ema_keeper.get())
            self.assertEqual(loaded_macd_keeper.data_count, self.macd_keeper.data_count)

if __name__ == "__main__":
    unittest.main()
