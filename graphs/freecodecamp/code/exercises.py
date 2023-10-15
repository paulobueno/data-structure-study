from collections import deque

# find path

cases = [([{'a': ['b', 'c'],
            'b': ['d'],
            'c': ['e'],
            'd': ['f'],
            'e': [],
            'f': []}, deque(['a'])], True)]


def depth_first_traversal(graph, d):
    if len(d) == 0:
        return False
    current = d.pop()
    if len(graph[current]) == 0:
        return True
    for neighbor in graph[current]:
        d.append(neighbor)
    if depth_first_traversal(graph, d):
        return True
    else:
        return False


print(depth_first_traversal(*cases[0][0]))
