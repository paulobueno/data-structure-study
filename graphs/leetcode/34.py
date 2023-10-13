import bisect
from time import time
from typing import List


def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.6f}s')
        return result

    return wrap_func


class ReviewAnswers:
    def __init__(self):
        self.cases = [([[5, 7, 7, 8, 8, 10], 8], [3, 4]),
                      ([[1], 1], [0, 0])]

    @timer_func
    def check_answers(self, func):
        for n, case in enumerate(self.cases):
            print(f'Case N{n}: ', func(*case[0]) == case[1])


def search_range_v1(nums: List[int], target: int) -> List[int]:
    start = bisect.bisect_left(nums, target)
    if start >= len(nums):
        return [-1, -1]
    elif target != nums[start]:
        return [-1, -1]
    end = bisect.bisect_right(nums, target) - 1
    return [start, end]


def search_range_v2(nums: List[int], target: int) -> List[int]:
    start = bisect.bisect_left(nums, target)
    end = start
    if start >= len(nums):
        return [-1, -1]
    elif target != nums[start]:
        return [-1, -1]

    while end < len(nums) - 1:
        if nums[end] == target:
            end += 1
        else:
            end -= 1
            break

    if nums[end] != target:
        end -= 1

    return [start, end]


if __name__ == '__main__':
    # O(2logN) solution
    ReviewAnswers().check_answers(search_range_v1)
    # O(logN) solution
    ReviewAnswers().check_answers(search_range_v2)
