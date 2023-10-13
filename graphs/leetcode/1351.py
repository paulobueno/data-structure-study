import bisect
from typing import List
from time import time


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
        self.cases = [([[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]], 8),
                      ([[[5, 1, 0], [-5, -5, -5]]], 3)]

    @timer_func
    def check_answers(self, func):
        for n, case in enumerate(self.cases):
            print(f'Case N{n}: ', func(*case[0]) == case[1])


def count_negatives(grid: List[List[int]]) -> int:
    count = 0
    for i, m in enumerate(grid):
        index = bisect.bisect(m, 0, key=lambda x: -x)
        count += len(m[index:])
        if index == 0:
            count += len(grid[i + 1:]) * len(grid[0])
            break
    return count


if __name__ == '__main__':
    ReviewAnswers().check_answers(count_negatives)
