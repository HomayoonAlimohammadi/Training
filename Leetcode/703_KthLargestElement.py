from typing import List, Optional
import heapq


class KthLargest:

    def __init__(self, k: int, values: List[int] = None) -> None:
        self.k = k
        if values:
            self.values = sorted(values, reverse=True)
        else:
            self.values = []

    def get_kth_element(self) -> int:
        if self.k <= len(self.values):
            return self.values[self.k-1]
        else:
            raise ValueError(f'K is larger than values length ({len(self.values)}). Pick a smaller one.')

    def add(self, value: int) -> int:
        self.reverse_insort(self.values, value)
        return self.get_kth_element()

    def __str__(self):
        return f'KthLargest --> k: {self.k}, List: {self.values}'

    def __repr__(self):
        result = '['
        for val in self.values[:3]:
            result += str(val) + ', '
        result = result[:-1] + '...]'
        return result

    def reverse_insort(self, li: List[int], value: int, low: int = 0, high: Optional[int] = None) -> None:
        '''
        Insert item x in list a, and keep it reverse-sorted assuming a is reverse-sorted. 
        If x is already in a, insert it to the right of the rightmost x.
        Optional args lo (default 0) and hi (default len(a)) bound the slice of a to be searched.
        '''

        if low < 0:
            raise ValueError('`low` must be non-negative')
        if high is None:
            high = len(li)

        while low < high:
            mid = (low + high) // 2
            if value > li[mid]:
                high = mid
            else:
                low = mid + 1
        li.insert(low, value)


class KthLargest2:

    def __init__(self, k: int, values: List[int] = None) -> None:
        self.k = k
        if values:
            self.values = values
            heapq.heapify(self.values)

            while len(self.values) > self.k:
                heapq.heappop(self.values)
        else:
            self.values = []

    def add(self, value: int) -> int:
        heapq.heappush(self.values, value)
        if len(self.values) > self.k:
            heapq.heappop(self.values)
        return self.values[0]


k = 3
values = [4,5,8,2]
obj = KthLargest2(k, values)
print(obj)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
