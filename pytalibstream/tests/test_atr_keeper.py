import unittest

from pytalibstream.atr_keeper import AtrKeeper
from pytalibstream.types.hlc import HLC


class TestAtrKeeper(unittest.TestCase):

    def setUp(self) -> None:
        self.atr_keeper = AtrKeeper(5)
        self.sample = range(1, 21)

    def test_add(self):
        for i in self.sample:
            candle = HLC.from_list([i + 1, i, i * .90])
            self.atr_keeper.add(candle)

    def test_get_tr(self):
        actual = AtrKeeper.get_tr(3, 1, 2)
        self.assertEqual(2, actual)
