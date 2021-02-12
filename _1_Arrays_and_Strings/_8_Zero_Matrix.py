# Jacob Wahl
# 2/8/21
# Problem 1.8 - Wrtie an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# -> list[list[int]]
def zeroMatrix(matrix: list[list[int]]) -> list[list[int]]:

    # Not in-place
    '''
    new_matrix = [[-1 for y in range(len(matrix[x]))]
                  for x in range(len(matrix))]

    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix):
            if matrix[i][j] == 0:
                new_matrix = zeroize(i, j, new_matrix)
            elif new_matrix[i][j] != 0:
                new_matrix[i][j] = matrix[i][j]
            j += 1
        i += 1

    return new_matrix
    '''

    # In-place
    rows = set()
    cols = set()

    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
            j += 1
        i += 1

    return zeroize(rows, cols, matrix)


def zeroize(row: set or int, col: set or int, matrix: list[list[int]]) -> list[list[int]]:

    if isinstance(row, set) and isinstance(col, set):
        for i in row:
            idx = 0
            while(idx < len(matrix[i])):
                matrix[i][idx] = 0
                idx += 1

        for i in col:
            idx = 0
            while(idx < len(matrix)):
                matrix[idx][i] = 0
                idx += 1

    else:

        idx = 0
        while(idx < len(matrix[row])):
            matrix[row][idx] = 0
            idx += 1

        idx = 0
        while(idx < len(matrix)):
            matrix[idx][col] = 0
            idx += 1

    return matrix


test_case = [[-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1]]
'''
test_case = [[-1, -1, -1],
             [-1, -1, -1],
             [-1, -1, -1]]
'''

test_case = zeroMatrix(test_case)

for i in test_case:
    print(i)
