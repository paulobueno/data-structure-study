from collections import deque
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
        self.cases = [([[[1, 2], [2, 3], [5], [0], [5], [], []]], [2, 4, 5, 6]),
                      ([[[], [0, 2, 3, 4], [3], [4], []]], [0, 1, 2, 3, 4]),
                      ([[[], [2], [1], [4], []]], [0, 3, 4])]

    @timer_func
    def check_answers(self, func):
        for n, case in enumerate(self.cases):
            print(f'Case N{n}: ', func(*case[0]) == case[1])


def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    safe = {}
    ans = []

    def dfs(i):
        if i in safe:
            return safe[i]

        safe[i] = False
        for nei in graph[i]:
            if not dfs(nei):
                return safe[i]

        safe[i] = True
        return safe[i]

    for i in range(n):
        if dfs(i):
            ans.append(i)

    return ans


# solution by Motaharozzaman1996
if __name__ == '__main__':
    ReviewAnswers().check_answers(eventual_safe_nodes)
