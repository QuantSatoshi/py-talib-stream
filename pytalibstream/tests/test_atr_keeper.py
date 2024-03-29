import pickle
import unittest

import numpy as np
import talib

from pytalibstream.atr_keeper import AtrKeeper


class TestAtrKeeper(unittest.TestCase):
    def setUp(self) -> None:
        self.atr_keeper = AtrKeeper(5)
        self.sample = np.random.uniform(1, 2, (30, 3))
        self.sample[:, 0] = self.sample[:, 0] + 1
        self.sample[:, 1] = self.sample[:, 1] - 1

    def test_add(self):
        atr_ta = talib.ATR(
            high=self.sample[:, 0], low=self.sample[:, 1], close=self.sample[:, 2], timeperiod=5
        )
        for i in range(0, len(self.sample)):
            self.atr_keeper.add(self.sample[i, :][0], self.sample[i, :][1], self.sample[i, :][2])

            if i > 20:
                self.assertTrue(
                    abs(self.atr_keeper.get() - atr_ta[i]) < 0.0001
                )

    def test_get_tr(self):
        actual = AtrKeeper.get_tr(3, 1, 2)
        self.assertEqual(2, actual)

    def test_pickle_dump(self):
        for i in range(0, len(self.sample)):
            self.atr_keeper.add(self.sample[i, :][0], self.sample[i, :][1], self.sample[i, :][2])
        # Serialize the instance to a file
   
        with open('atr_keeper.pickle', 'wb') as file:
            pickle.dump(self.atr_keeper, file)

        # Deserialize the instance from the file
        with open('atr_keeper.pickle', 'rb') as file:
            loaded_atr_keeper = pickle.load(file)
            self.assertEqual(loaded_atr_keeper.get(), self.atr_keeper.get())
            self.assertEqual(loaded_atr_keeper.high.first(), self.atr_keeper.high.first())
            self.assertEqual(loaded_atr_keeper.high.last(), self.atr_keeper.high.last())
            self.assertEqual(loaded_atr_keeper.high.length(), self.atr_keeper.high.length())
            self.assertEqual(loaded_atr_keeper.low.first(), self.atr_keeper.low.first())
            self.assertEqual(loaded_atr_keeper.low.last(), self.atr_keeper.low.last())
            self.assertEqual(loaded_atr_keeper.close.first(), self.atr_keeper.close.first())
            self.assertEqual(loaded_atr_keeper.close.last(), self.atr_keeper.close.last())

    