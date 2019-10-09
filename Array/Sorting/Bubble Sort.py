
class Solution:
    def bubbleSort(self, arr):
        arrayLength = len(arr)

        for i in range(arrayLength):
            for j in range(0, arrayLength-i-1):
                if (arr[j] > arr[j + 1]):
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        return arr


if __name__ == "__main__":
    unsortedArray = [64, 34, 25, 12, 22, 11, 90]
    print("The sorted array is")
    print(Solution().bubbleSort(unsortedArray))
