cases = [(([-1, 0, 3, 5, 9, 12], 9), 4),
         (([-1, 0, 3, 5, 9, 12], 2), -1)]


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums)

    while start < end:
        median = ((end - start) // 2) + start
        if target == nums[median]:
            return median

        if target > nums[median]:
            start = median + 1
        else:
            end = median

    return -1


if __name__ == '__main__':
    for n, case in enumerate(cases):
        print(f'Case N{n}: ', search(case[0][0], case[0][1]) == case[1])
