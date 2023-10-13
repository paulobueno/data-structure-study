cases = [(([1, 3, 5, 6], 7), 4),
         (([1, 3, 5, 6], 2), 1),
         (([1, 3, 5, 6], -1), 0)]


def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums)

    while start < end:
        middle = ((end - start) // 2) + start
        if target == nums[middle]:
            return middle
        if target > nums[middle]:
            start = middle + 1
        else:
            end = middle

    if start == end:
        return start
    elif nums[start] < target < nums[end]:
        return end
    elif target < nums[start]:
        return start - 1
    elif target > nums[end]:
        return end + 1


if __name__ == '__main__':
    for n, case in enumerate(cases):
        print(f'Case N{n}: ', search_insert(case[0][0], case[0][1]) == case[1])
