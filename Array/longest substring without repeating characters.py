# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a string, find the length of the longest substring without repeating characters.

# class Solution:
#   def lengthOfLongestSubstring(self, s):
#     # Fill this in.

# print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# # 10

# Can you find a solution in linear time?


class Solution:
    def lengthOfLongestSubstring(self, str):
        NO_OF_CHARACTERS = 256
        visitedCharacters = [-1] * NO_OF_CHARACTERS
        visitedIndex = 0
        longestSubstring = ''
        newSubstring = ''

        for character in str:
            if (visitedCharacters[ord(character)] == -1):
                visitedCharacters[ord(character)] = 0
                newSubstring = newSubstring + character
                visitedIndex += 1
            elif(len(newSubstring) > len(longestSubstring)):
                longestSubstring = newSubstring
                newSubstring = ""

        return longestSubstring


string = raw_input()
result = Solution().lengthOfLongestSubstring(string)
print "length of the longest substring without repeating characters " + \
    str(result)
