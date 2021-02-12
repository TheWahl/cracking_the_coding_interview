# Jacob Wahl
# 1/29/21
# Problem 1.3 - Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,
#               and that you are given the 'true' length of the string.
#
#   Ex. Input : "Mr John Smith    ", 13
#       Output: "Mr%20John%20Smith"

def replaceSpaceHTML(string: str) -> str:
    return string.strip().replace(' ', '%20')


print(replaceSpaceHTML('I am Jake Wahl       '))
