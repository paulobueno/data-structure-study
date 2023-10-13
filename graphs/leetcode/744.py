import bisect
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
        self.cases = [((["c", "f", "j"], "a"), "c"),
                      ((["c", "f", "j"], "c"), "f"),
                      ((["x", "x", "y", "y"], "z"), "x")]

    @timer_func
    def check_answers(self, func):
        for n, case in enumerate(self.cases):
            print(f'Case N{n}: ', func(*case[0]) == case[1])


def next_greatest_letter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """

    start = 0
    end = len(letters) - 1

    while start < end:
        middle = ((end - start) // 2) + start
        if letters[middle] == target:
            break
        if target > letters[middle]:
            start = middle + 1
        else:
            end = middle

    middle = ((end - start) // 2) + start

    while middle < len(letters) - 1:
        if letters[middle] == target:
            middle += 1
        else:
            break

    if target < letters[middle]:
        return letters[middle]
    elif middle == len(letters) - 1:
        return letters[0]
    elif target > letters[middle]:
        return letters[middle + 1]
    else:
        return letters[0]


def next_greatest_letter_v2(letters, target):
    return letters[bisect.bisect(letters, target) % len(letters)]


if __name__ == '__main__':
    ReviewAnswers().check_answers(next_greatest_letter)
    ReviewAnswers().check_answers(next_greatest_letter_v2)
