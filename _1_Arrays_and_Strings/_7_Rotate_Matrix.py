# Jacob Wahl
# 2/4/21
# Problem 1.7 - Given an image represnted by an NxN matrix, where each pixel in the image is 4 bytes,
#               write a method to rotate the image by 90 degrees. Can you do this in place?


# Using ints instead of 4 bytes because the method should be the same in essence
# Assuming clockwise rotaion
def rotateImage(matrix):

    N = len(matrix)

    # Not in place
    '''
    new_matrix = [[0 for x in range(N)] for x in range(N)]

    i = 0
    while i < N:
        j = 0
        while j < N:
            new_matrix[j][(N-1) - i] = matrix[i][j]
            j += 1
        i += 1

    return new_matrix
    '''

    # In place

    if N % 2 == 0:
        for Sr in range(0, N//2 - 1):
            Sc = Sr
            Fc = N - 2 - Sc

            length = Fc - Sc + 1

            Top = (Sr, Sc)
            Right = (Sr, Fc + 1)
            Bot = (N - 1 - Sr, Fc + 1)
            Left = (N - 1 - Sr, Sc)

            for i in range(length):
                tmp = matrix[Top[0]][Top[1] + i]
                matrix[Top[0]][Top[1] + i] = matrix[Left[0] - i][Left[1]]
                matrix[Left[0] - i][Left[1]] = matrix[Bot[0]][Bot[1] - i]
                matrix[Bot[0]][Bot[1] - i] = matrix[Right[0] + i][Right[1]]
                matrix[Right[0] + i][Right[1]] = tmp

            tmp = matrix[N//2 - 1][N//2 - 1]
            matrix[N//2 - 1][N//2 - 1] = matrix[N//2][N//2 - 1]
            matrix[N//2][N//2 - 1] = matrix[N//2][N//2]
            matrix[N//2][N//2] = matrix[N//2 - 1][N//2]
            matrix[N//2 - 1][N//2] = tmp

    else:
        for Sr in range(0, max(1, N//2 - 1)):
            Sc = Sr
            Fc = N - 2 - Sc

            length = Fc - Sc + 1

            Top = (Sr, Sc)
            Right = (Sr, Fc + 1)
            Bot = (N - 1 - Sr, Fc + 1)
            Left = (N - 1 - Sr, Sc)

            for i in range(length):
                tmp = matrix[Top[0]][Top[1] + i]
                matrix[Top[0]][Top[1] + i] = matrix[Left[0] - i][Left[1]]
                matrix[Left[0] - i][Left[1]] = matrix[Bot[0]][Bot[1] - i]
                matrix[Bot[0]][Bot[1] - i] = matrix[Right[0] + i][Right[1]]
                matrix[Right[0] + i][Right[1]] = tmp

    return matrix


test_case = [['h', 'd', 'a'],
             ['i', 'e', 'b'],
             ['j', 'f', 'c']]

z = 0
while z < 4:
    test_case = rotateImage(test_case)

    for i in test_case:
        print(i)
    print()
    z += 1
