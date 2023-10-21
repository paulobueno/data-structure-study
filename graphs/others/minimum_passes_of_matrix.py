def get_negative_indexes(matrix):
    output = set()
    for i, row in enumerate(matrix):
        for j, number in enumerate(row):
            if number < 0:
                output.add((i, j))
    return output


def can_be_flipped(i, j, matrix):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    i_max = len(matrix) - 1
    j_max = len(matrix[0]) - 1
    for move in moves:
        new_i = i + move[0]
        new_j = j + move[1]
        if (0 <= new_i <= i_max) and (0 <= new_j <= j_max):
            if matrix[new_i][new_j] > 0:
                return True


def minimum_passes_of_matrix(matrix):
    negative_indexes = get_negative_indexes(matrix)
    aux_matrix = None
    iterations = 0

    if len(negative_indexes) == 0:
        return 0

    while True:

        if aux_matrix is None:
            aux_matrix = [row[:] for row in matrix]
        else:
            matrix = [row[:] for row in aux_matrix]

        for negative_index in list(negative_indexes):
            i, j = negative_index
            if can_be_flipped(i, j, matrix):
                negative_indexes.remove(negative_index)
                aux_matrix[i][j] *= -1

        if aux_matrix != matrix:
            iterations += 1
        else:
            break

    if len(negative_indexes) > 0:
        return -1
    else:
        return iterations


if __name__ == '__main__':
    print(minimum_passes_of_matrix([
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1]
    ]) == 3)
