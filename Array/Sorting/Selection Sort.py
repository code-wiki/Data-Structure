
class Solution:
    def selectionSort(self, arr):
        arrayLength = len(arr)

        for i in range(arrayLength):
            for j in range(arrayLength-1):


if __name__ == "__main__":
    unsortedArray = [64, 34, 25, 12, 22, 11, 90]
    print("The sorted array is")
    print(Solution().bubbleSort(unsortedArray))
