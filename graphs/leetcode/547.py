from itertools import combinations

cases = [([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
         ([[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]], 3)]


class Solution:
    @staticmethod
    def merge_connections(connections1, connections2):
        temp = []
        for comp in zip(connections1, connections2):
            if comp[0] == 1 or comp[1] == 1:
                temp.append(1)
            else:
                temp.append(0)
        return temp

    def manipulate_is_connected(self, is_connected):
        size = len(is_connected)
        for city_index_1, city_index_2 in combinations(range(size), 2):
            for i in range(len(is_connected[0])):
                if is_connected[city_index_1][i] == 1 and is_connected[city_index_2][i] == 1:
                    is_connected[city_index_1] = self.merge_connections(is_connected[city_index_1],
                                                                        is_connected[city_index_2])
                    del is_connected[city_index_2]
                    return is_connected

    def find_circle_num(self, is_connected):
        """
        :type is_connected: List[List[int]]
        :rtype: int
        """
        keep_running = True
        while keep_running:
            if self.manipulate_is_connected(is_connected) is None:
                keep_running = False
        return len(is_connected)


if __name__ == '__main__':
    for i, case in enumerate(cases):
        print(f"Case N {i}: ", Solution().find_circle_num(case[0]) == case[1])
