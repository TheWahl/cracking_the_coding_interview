# Jacob Wahl
# 2/8/21
# Problem 1.9 - Assume you have a method 'isSubstring' which checks if on word is a substring of another.
#               Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
#               call to 'isSubstring'
#
# Ex: 'waterbottle' is a rotation of 'erbottlewat'

def isRotation(s1: str, s2: str) -> bool:
    '''
    if s1 == s2:
        return True

    if len(s1) != len(s2):
        return False

    dict1, dict2 = {}, {}
    for letter in s1:
        dict1[letter] = dict1.get(letter, 0) + 1
    for letter in s2:
        dict2[letter] = dict2.get(letter, 0) + 1

    if dict1 != dict2:
        return False

    # Go through and validate that letters are in the same order
    '''

    if len(s1) != len(s2):
        return False

    repeated = s2 + s2
    return isSubstring(repeated, s1)


def isSubstring(a: str, b: str) -> bool:
    return b in a


a = 'aa'
b = 'aa'
print(isRotation(a, b))
