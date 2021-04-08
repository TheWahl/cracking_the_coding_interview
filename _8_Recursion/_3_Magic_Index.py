# Jacob Wahl
# 4/6/21
#
# Problem 8.3 - A magic index in an array A[0 ... n-1] is defined to be an
#               index such that A[i] = i. Given a sorted array of distinct,
#               write a method to find a magic index, if one exists, in array
#               A.
#               FOLLOW UP: What if the values are not distinct?


def find_magic_idnex(A):
    return find_magic_index_recurse_follow_up(A, 0, len(A)-1)


'''
def find_magic_index_recurse(A, start, stop):

    if start > stop:
        return False

    middle = (stop - start // 2) + start
    if A[middle] == middle:
        return middle
    elif A[middle] < middle:
        return find_magic_index_recurse(A, middle+1, stop)
    else:
        return find_magic_index_recurse(A, start, middle-1)
'''


def find_magic_index_recurse_follow_up(A, start, stop):

    if start > stop:
        return -1

    middle = (stop - start // 2) + start
    if A[middle] == middle:
        return middle

    rightIdx = min(A[middle], middle-1)
    result = find_magic_index_recurse_follow_up(A, start, rightIdx)

    if result != -1:
        return result

    leftIdx = max(middle+1, A[middle])
    result = find_magic_index_recurse_follow_up(A, leftIdx, stop)

    return result


'''
test_cases = [[0, 4, 7, 9, 10], [-1, 1, 11, 22, 33], 
            [-2, 0, 2, 23, 45], [-22, -9, -10, 3, 20], [-6, -3, 0, 2, 4],
            [-1, 0, 0, 0, 0], [55, 60, 75, 78, 99]]
'''
test_cases = [-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13]


print(find_magic_idnex(test_cases))
