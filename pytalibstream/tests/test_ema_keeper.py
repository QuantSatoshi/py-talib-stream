import pickle
import unittest

from pytalibstream.ema_keeper import EmaKeeper


class TestEmaKeeper(unittest.TestCase):
    def setUp(self) -> None:
        self.ema_keeper = EmaKeeper(3)

    def test_add(self):
        self.ema_keeper.add(1)
        self.assertEqual(self.ema_keeper.ema, 1)
        self.ema_keeper.add(2)
        self.ema_keeper.add(3)
        self.assertEqual(self.ema_keeper.ema, 2)

    def test_get_ema(self):
        for i in range(1, 5):
            self.ema_keeper.add(i)
        self.assertEqual(self.ema_keeper.ema, 3)
        
    def test_pickle_dump(self):
        self.ema_keeper.add(1)
        self.ema_keeper.add(2)
        self.ema_keeper.add(3)

        # Serialize the instance to a file
   
        with open('ema_keeper.pickle', 'wb') as file:
            pickle.dump(self.ema_keeper, file)

        # Deserialize the instance from the file
        with open('ema_keeper.pickle', 'rb') as file:
            loaded_sma_keeper = pickle.load(file)
            self.assertEqual(loaded_sma_keeper.get(), self.ema_keeper.get())