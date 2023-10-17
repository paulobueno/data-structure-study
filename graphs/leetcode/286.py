from typing import List

def walls_and_gates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    max_i = len(rooms) - 1
    max_j = len(rooms[0]) - 1
    gates = []
    for i, row in enumerate(rooms):
        for j, room in enumerate(row):
            if room == 0:
                gates.append((i, j))

    def build_steps(i, j, n=None, visited_room=None):
        if n is None:
            n = 0
            visited_room = set()
        rooms[i][j] = min(n, rooms[i][j])

        if rooms[i][j] <= 0 < n:
            return
        elif (i, j) in visited_room:
            return

        visited_room.add((i, j))

        n += 1
        if i < max_i:
            build_steps(i + 1, j, n, visited_room)
        if j < max_j:
            build_steps(i, j + 1, n, visited_room)
        if i > 0:
            build_steps(i - 1, j, n, visited_room)
        if j > 0:
            build_steps(i, j - 1, n, visited_room)

    for i, j in gates:
        build_steps(i, j)


rooms = [[2147483647, -1, 0, 2147483647],
         [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]]

if __name__ == '__main__':
    walls_and_gates(rooms)
    print(rooms)
