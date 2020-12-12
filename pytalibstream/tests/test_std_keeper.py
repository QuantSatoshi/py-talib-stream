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


if __name__ == "__main__":
    unittest.main()
