cases = [((["c", "f", "j"], "a"), "c"),
         ((["c", "f", "j"], "c"), "f"),
         ((["x", "x", "y", "y"], "z"), "x")]


def next_greatest_letter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """

    start = 0
    end = len(letters) - 1
    middle = None

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


if __name__ == '__main__':
    for n, case in enumerate(cases):
        print(f'Case N{n}: ', next_greatest_letter(case[0][0], case[0][1]) == case[1])
