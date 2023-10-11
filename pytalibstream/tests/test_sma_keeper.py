import pickle
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

    def test_pickle_dump(self):
        sma_keeper = SmaKeeper(3)
        sma_keeper.add(1)
        sma_keeper.add(2)
        sma_keeper.add(3)
        sma_keeper.add(4)
        # Serialize the instance to a file
   
        with open('sma_keeper.pickle', 'wb') as file:
            pickle.dump(sma_keeper, file)

        # Deserialize the instance from the file
        with open('sma_keeper.pickle', 'rb') as file:
            loaded_sma_keeper = pickle.load(file)
            self.assertEqual(loaded_sma_keeper.get(), sma_keeper.get())
            self.assertEqual(loaded_sma_keeper.arr.first(), sma_keeper.arr.first())
            self.assertEqual(loaded_sma_keeper.arr.last(), sma_keeper.arr.last())
            self.assertEqual(loaded_sma_keeper.arr.length(), sma_keeper.arr.length())

if __name__ == "__main__":
    unittest.main()
