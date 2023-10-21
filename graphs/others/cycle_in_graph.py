def cycle_in_graph(edges):
    for node_index, edge_list in enumerate(edges):
        for edge in edge_list:
            stack = [edge]
            visited_nodes = [False for _ in edges]
            visited_nodes[node_index] = True

            while len(stack) > 0:
                current_node = stack.pop()

                if visited_nodes[current_node]:
                    return True
                else:
                    visited_nodes[current_node] = True

                stack += edges[current_node]

    return False


if __name__ == '__main__':
    cycle_in_graph([
        [],
        [0, 2],
        [0, 3],
        [0, 4],
        [0, 5],
        [0]
    ])
