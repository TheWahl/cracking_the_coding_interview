# Jacob Wahl
# 1/27/21
# Problem 1.1 - Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUniqueString(string: str, useStructure=True) -> bool:

    # Using dictionary
    if useStructure:
        letters = {}
        for c in string:
            count = letters.get(c, 0)
            if count == 0:
                letters[c] = 1
            else:
                return False
        return True

    # Not using data structures
    else:
        for i, c in enumerate(string):
            print(i, c)
            if c in string[i+1:]:
                return False
        return True


if __name__ == "__main__":
    string = 'aaba'
    print(isUniqueString(string, False))
