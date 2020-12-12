import unittest

from pytalibstream.sma_keeper import SmaKeeper


class TestSmaKeeper(unittest.TestCase):
    def test_basic(self):
        sma_keeper = SmaKeeper(3)
        sma_keeper.add(1)
        assert sma_keeper.get() == 1
        sma_keeper.add(2)
        sma_keeper.add(3)
        assert sma_keeper.get() == 2
        sma_keeper.add(4)
        assert sma_keeper.get() == 3


if __name__ == "__main__":
    unittest.main()