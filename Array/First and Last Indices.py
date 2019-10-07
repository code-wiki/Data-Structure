# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given a sorted array, A,
# with possibly duplicated elements,
# find the indices of the first and last occurrences of a target element, x.
# Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]


class Solution:
    def checkIndices(self, inputArray, key):
        startIndices = -1
        endIndices = -1
        count = 0

        for elem in inputArray:
            print(elem)
            if (elem == key):
                if (startIndices == -1):
                    startIndices = count
                else:
                    endIndices = count
            count += 1

        return (startIndices, endIndices)


if __name__ == "__main__":
    inputArray = [9, 9, 11, 11, 12, 12, 13]
    searchKey = 11
    indices = Solution().checkIndices(inputArray, searchKey)
    print(indices)
