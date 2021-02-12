# Jacob Wahl
# 2/4/21
# Problem 1.6 - Implement a method to perform basic string compression using the counts or repeated characters.
#               For example, the string aabcccccaaa would become a2b1c5a3. If the 'compressed' string would not
#               become smaller than the original string, you method should reutrn the original string. You can
#               assume the string only contains letters.

def compressString(string: str) -> str:

    original_len = len(string)
    new_string = ''
    prev_char = ''
    char_count = 0

    for char in string:
        if not prev_char:
            prev_char = char
            char_count = 1
        elif char == prev_char:
            char_count += 1
        elif char != prev_char:
            new_string += prev_char + str(char_count)
            prev_char = char
            char_count = 1
    else:
        new_string += prev_char + str(char_count)

    if len(new_string) < original_len:
        return new_string
    else:
        return string


test_cases = ['aaaaabbbbbcdddrrrrttg',
              'ab']

for i in test_cases:
    print(compressString(i), )
