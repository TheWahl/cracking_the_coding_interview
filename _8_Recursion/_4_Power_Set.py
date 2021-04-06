# Jacob Wahl
# 4/5/21
#
# Problem 8.4 - Write a method to return all subsets of a set
#

def subset(li: list) -> list:
    return subsetRecursive(li, [])


def subsetRecursive(li: list, sets: list):
    # Base Case
    if not li:
        return

    # Recursive Case
    if li not in sets:
        sets.append([x for x in li])

    for i in range(len(li)):
        cur = li.pop(i)
        subsetRecursive(li, sets)
        li.insert(i, cur)

    return sets


li = [1, 2, 3, 4, 5, 6]
sets = subset(li)
sets.sort(key=lambda x: len(x), reverse=True)
for i in sets:
    print(i)
