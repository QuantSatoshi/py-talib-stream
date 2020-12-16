import unittest

from pytalibstream.atr_keeper import AtrKeeper


class TestAtrKeeper(unittest.TestCase):

    def setUp(self) -> None:
        self.atr_keeper = AtrKeeper(5)
        self.sample = range(1, 21)

    def test_add(self):
        for i in self.sample:
            self.atr_keeper.add(i + 1, i, i * .90)

        self.assertEqual(3.5, round(self.atr_keeper.atr, 1))

    def test_get_tr(self):
        actual = AtrKeeper.get_tr(3, 1, 2)
        self.assertEqual(2, actual)
