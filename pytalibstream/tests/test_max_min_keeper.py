import pickle
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

    def test_pickle_dump(self):
        self.max_min_keeper.add(1)
        self.max_min_keeper.add(2)
        self.max_min_keeper.add(3)
        self.max_min_keeper.add(4)
        # Serialize the instance to a file
   
        with open('max_min_keeper.pickle', 'wb') as file:
            pickle.dump(self.max_min_keeper, file)

        # Deserialize the instance from the file
        with open('max_min_keeper.pickle', 'rb') as file:
            loaded_sma_keeper = pickle.load(file)
            self.assertEqual(loaded_sma_keeper.max, self.max_min_keeper.max)
            self.assertEqual(loaded_sma_keeper.min, self.max_min_keeper.min)
            self.assertEqual(loaded_sma_keeper.arr.first(), self.max_min_keeper.arr.first())
            self.assertEqual(loaded_sma_keeper.arr.last(), self.max_min_keeper.arr.last())
            self.assertEqual(loaded_sma_keeper.arr.length(), self.max_min_keeper.arr.length())
  