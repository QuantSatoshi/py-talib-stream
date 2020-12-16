import unittest

from pytalibstream.macd_keeper import MacdKeeper


class TestMacdKeeper(unittest.TestCase):

    def setUp(self) -> None:
        self.macd_keeper = MacdKeeper(12, 26, 9)
        self.sample = range(1, 101)

    def test_add(self):
        self.macd_keeper.add(10)
        self.assertEqual(self.macd_keeper.slow_ema_keeper.arr.length(), 1)

    def test_macd(self):
        for i in self.sample:
            self.macd_keeper.add(i)
        self.assertEqual(self.macd_keeper.macd['macd'], 7)
