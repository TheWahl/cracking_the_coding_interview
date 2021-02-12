# Jacob Wahl
# 1/28/21
# Problem 1.2 - Given two stings, write a method to deicde if one is a permutation of the other.

def isPermutation(a: str, b: str, useStructure=True) -> bool:

    if len(a) != len(b):
        return False

    a = list(a)
    b = list(b)

    # Using Dictionary
    if useStructure:

        letters1 = {}
        letters2 = {}

        for c in a:
            count = letters1.get(c, 0)
            letters1[c] = (count + 1)
        for c in b:
            count = letters2.get(c, 0)
            letters2[c] = (count + 1)

        if letters1 == letters2:
            return True
        else:
            return False

    # Using loops
    else:

        for idx in range(len(a)):
            char = a[idx]
            try:
                b.index(char)  # Could throw exception
                b.remove(char)
            except ValueError:
                return False

        return True


if __name__ == "__main__":
    test_cases = [
        ('', ''),               # True
        ('abcde', 'abcdef'),    # False
        ('abcde', 'abcde'),     # True
        ('zbcde', 'abcde'),     # False
        ('abcdz', 'abcde'),     # False
        ('abzde', 'abcde')]    # False

    for i in test_cases:
        print(isPermutation(i[0], i[1], False))
        print(isPermutation(i[1], i[0], False))
        print()
