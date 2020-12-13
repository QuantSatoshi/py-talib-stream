import unittest

from pytalibstream.ema_keeper import EmaKeeper


class TestEmaKeeper(unittest.TestCase):

    def setUp(self) -> None:
        self.ema_keeper = EmaKeeper(3)

    def test_add(self):
        self.ema_keeper.add(1)
        self.assertEqual(self.ema_keeper.ema, 0)
        self.ema_keeper.add(2)
        self.ema_keeper.add(3)
        self.assertEqual(self.ema_keeper.ema, 2)

    def test_get_ema(self):
        for i in range(1, 5):
            self.ema_keeper.add(i)
        self.assertEqual(self.ema_keeper.ema, 3)
