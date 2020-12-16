from collections import namedtuple
from typing import List


class HLC(namedtuple('HLC', 'high low close')):
    """namedtuple for high, low, and close values"""

    @staticmethod
    def from_list(values: List[float]):
        if len(values) == 0: return None
        return HLC(max(values), min(values), values[-1])
