# Jacob Wahl
# 1/29/21
# Problem 1.4 - Given a string, write a function to check if it is a permutation of a palindrome.
#
# Ex. Input: Tact Coa
#     Output: True (taco cat, atco cta, etc.)

def isPalindromePermutation(string: str, useStructure=True) -> bool:
    string = string.replace(' ', '')
    string = list(string)

    # Using Dictionary
    if useStructure:
        letter_count = {}
        no_match = 0

        for a in string:
            letter_count[a] = (letter_count.get(a, 0) + 1)

        for key in letter_count:
            if letter_count[key] % 2 != 0:
                no_match += 1
            if no_match == 2:
                return False
        return True

    # Using Loops
    else:
        no_match = 0

        while True:
            if no_match > 1:
                return False

            if string:
                char = string.pop(0)
                try:
                    string.index(char)  # Could throw exception
                    string.remove(char)
                except ValueError:
                    no_match += 1
                    if no_match > 1:
                        return False
            else:
                return True


if __name__ == "__main__":
    test_cases = [
        '',         # True
        'taco cat',  # True
        'aabbc',    # True
        'aabb',     # True
        'aabbce',   # False
        'aabc'     # False
    ]

    for i in test_cases:
        print(isPalindromePermutation(i))
        print()
