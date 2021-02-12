# Jacob Wahl
# 2/3/21
# Problem 1.5 - There are three types of edits that can be performed on strings: insert a char, remove a char, or replace a char.
#               Given two strings, write a function to check if they are one edit (or zero edits) away from one another.

def oneAway(a: str, b: str) -> bool:

    a_index = 0
    b_index = 0
    if len(a) == len(b):
        mismatch_found = False

        while a_index < len(a) and b_index < len(b):
            if a[a_index] != b[b_index]:
                if mismatch_found:
                    return False
                mismatch_found = True
            a_index += 1
            b_index += 1
        return True

    elif len(a) - 1 == len(b):
        missing_found = False

        while a_index < len(a) and b_index < len(b):
            if a[a_index] != b[b_index]:
                if missing_found:
                    return False
                a_index += 1
                missing_found = True
            else:
                a_index += 1
                b_index += 1
        return True

    elif len(a) == len(b) - 1:
        missing_found = False

        while a_index < len(a) and b_index < len(b):
            if a[a_index] != b[b_index]:
                if missing_found:
                    return False
                b_index += 1
                missing_found = True
            else:
                a_index += 1
                b_index += 1
        return True

    else:
        return False


test_cases = [('', ''),
              ('bc', 'abc'),  # True
              ('ac', 'abc'),
              ('ab', 'abc'),
              ('abc', 'zbc'),
              ('abc', 'azc'),
              ('abc', 'abz'),

              ('abczz', 'abc'),  # False
              ('abczz', 'abccc')]

for i, j in test_cases:
    print(oneAway(i, j))
    print(oneAway(j, i))
    print()
