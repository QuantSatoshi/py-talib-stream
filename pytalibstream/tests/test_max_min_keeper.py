import unittest

from pytalibstream.max_min_keeper import MaxMinKeeper


class TestMaxMinKeeper(unittest.TestCase):
    def setUp(self) -> None:
        self.max_min_keeper = MaxMinKeeper(3)
        self.sample = [10, 11, 9, 5, 4, 3]

    def test_add(self):
        for i in self.sample:
            self.max_min_keeper.add(i)

        self.assertEqual(3, self.max_min_keeper.min)
        self.assertEqual(5, self.max_min_keeper.max)
