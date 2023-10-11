import pickle
import unittest

from pytalibstream.std_keeper import StdKeeper


def std(values):
    mean = sum(values) / len(values)
    variance = sum([((x - mean) ** 2) for x in values]) / len(values)
    res = variance ** 0.5
    return res


class TestStdKeeper(unittest.TestCase):
    def test_basic(self):
        s = StdKeeper(3)
        s.add(1)
        s.add(2)

        assert s.get() == std([1, 2])
        s.add(5)
        assert s.get() == std([1, 2, 5])

        s.add(8)
        assert s.get() == std([2, 5, 8])
    
    def test_pickle_dump(self):
        std_keeper = StdKeeper(3)
        std_keeper.add(1)
        std_keeper.add(2)
        std_keeper.add(3)
        std_keeper.add(4)
        # Serialize the instance to a file
   
        with open('std_keeper.pickle', 'wb') as file:
            pickle.dump(std_keeper, file)

        # Deserialize the instance from the file
        with open('std_keeper.pickle', 'rb') as file:
            loaded_std_keeper = pickle.load(file)
            self.assertEqual(loaded_std_keeper.get(), std_keeper.get())
            self.assertEqual(loaded_std_keeper.arr.first(), std_keeper.arr.first())
            self.assertEqual(loaded_std_keeper.arr.last(), std_keeper.arr.last())
            self.assertEqual(loaded_std_keeper.arr.length(), std_keeper.arr.length())

if __name__ == "__main__":
    unittest.main()
