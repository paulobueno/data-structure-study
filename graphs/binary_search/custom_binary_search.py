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
    def __init__(self, cases):
        self.cases = cases

    @timer_func
    def check_answers(self, func):
        for n, case in enumerate(self.cases):
            print(f'Case N{n}: ', func(*case[0]) == case[1])


bisec_cases = [([[1, 4, 15, 22, 34, 49], 8], 2),
               ([[1, 4, 15, 22, 34, 49], 4], 1),
               ([[1, 4, 15, 22, 34, 49], 1], 0),
               ([[1, 4, 15, 22, 34, 49], -1], 0),
               ([[1, 4, 15, 22, 34, 49], 60], 6),
               ([[1, 4, 15, 22, 22, 22, 22, 22, 22, 22, 34, 49], 22], 3),
               ([[22, 22, 22, 22, 22, 22, 22], 22], 0),
               ([[22, 22, 22, 22, 22, 22, 22], 20], 0)]


def bisect(elements, target):
    lo = 0
    hi = len(elements)
    while lo < hi:
        mid = (lo + hi) // 2
        if target > elements[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo


found_element_cases = [([[1, 4, 15, 22, 34, 49], 8], False),
                       ([[1, 4, 15, 22, 34, 49], 4], True),
                       ([[1, 4, 15, 22, 34, 49], 1], True),
                       ([[1, 4, 15, 22, 34, 49], -1], False),
                       ([[1, 4, 15, 22, 34, 49], 60], False),
                       ([[1, 4, 15, 22, 22, 22, 22, 22, 22, 22, 34, 49], 22], True),
                       ([[22, 22, 22, 22, 22, 22, 22], 22], True),
                       ([[22, 22, 22, 22, 22, 22, 22], 20], False)]


def found_element(elements, target):
    size = len(elements)
    index = bisect(elements, target)
    if size == index:
        return False
    elif elements[index] == target:
        return True
    else:
        return False


if __name__ == '__main__':
    ReviewAnswers(bisec_cases).check_answers(bisect)
    ReviewAnswers(found_element_cases).check_answers(found_element)
