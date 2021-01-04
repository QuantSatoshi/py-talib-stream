from collections import deque

import pyslidingwindow


class MaxMinKeeper:
    def __init__(self, max_len: int):
        self.arr = pyslidingwindow.SlidingWindowFloat(max_len)
        self.max_arr = deque()
        self.min_arr = deque()

    def add_tail(self, value: float):
        while len(self.min_arr) > 0 and value < self.min_arr[-1]:
            self.min_arr.pop()
        self.min_arr.append(value)

        while len(self.max_arr) > 0 and value > self.max_arr[-1]:
            self.max_arr.pop()
        self.max_arr.append(value)

    def remove_head(self, value: float):
        if value < self.min_arr[0]:
            raise Exception(
                "wrong min_arr value {} min={}".format(value, self.min_arr[0])
            )
        elif value == self.min_arr[0]:
            self.min_arr.popleft()

        if value > self.max_arr[0]:
            raise Exception(
                "wrong max_arr value {} max={}".format(value, self.max_arr[0])
            )
        elif value == self.max_arr[0]:
            self.max_arr.popleft()

    def add(self, value: float):
        if self.arr.length() == self.arr.max_len():
            self.remove_head(self.arr.first())
        self.add_tail(value)
        self.arr.push(value)

    @property
    def min(self):
        if len(self.min_arr) < 0:
            raise Exception("Empty array")
        else:
            return self.min_arr[0]

    @property
    def max(self):
        if len(self.max_arr) < 0:
            raise Exception("Empty array")
        else:
            return self.max_arr[0]

    def debug(self):
        print("max={} min={}".format(self.max, self.min))
