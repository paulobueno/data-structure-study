# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    nodes = [descendantOne, descendantTwo]
    visited_nodes = set()
    match_node = None

    while match_node is None:
        for i, node in enumerate(nodes):
            if node in visited_nodes:
                match_node = node
                break
            visited_nodes.add(node)
            if node.ancestor:
                nodes[i] = node.ancestor

    return match_node

