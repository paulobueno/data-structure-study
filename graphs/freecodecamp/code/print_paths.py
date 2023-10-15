from collections import deque

# Depth First Traversal & Breadth First Traversal
# printing based on each technique

graph_data = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

answers = {'depth': 'acebdf',
           'breadth': 'abcdef'}


def depth_first_transversal(graph, start_point):
    def add_to_deque(de, elements):
        for element in elements:
            de.append(element)

    d = deque([start_point])
    output = ''

    while len(d) > 0:
        popped = d.pop()
        output += popped
        add_to_deque(d, graph[popped])

    return output


def depth_first_transversal_recursion(graph, d, path=''):
    if len(d) == 0:
        return path
    popped = d.pop()
    path += popped
    for neighbor in graph[popped]:
        d.append(neighbor)
    return depth_first_transversal_recursion(graph, d, path)


def breadth_first_transversal_recursion(graph, d, path=''):
    if len(d) == 0:
        return path
    popped = d.popleft()
    path += popped
    for neighbor in graph[popped]:
        d.append(neighbor)
    return breadth_first_transversal_recursion(graph, d, path)


if __name__ == '__main__':
    print(depth_first_transversal(graph_data, 'a'))
    print(depth_first_transversal_recursion(graph_data, deque(['a'])))
    print(breadth_first_transversal_recursion(graph_data, deque(['a'])))
