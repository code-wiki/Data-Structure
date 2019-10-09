class Solution:
    def insertionSort(self, arr):
        arrayLength = len(arr)
        for i in range(1, arrayLength):
            key = arr[i]
            j = i-1
            while (j >= 0 and key < arr[j]):
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = key
        return arr


if __name__ == "__main__":
    unsortedArray = [64, 34, 25, 12, 22, 11, 90]
    print("The sorted array is")
    print(Solution().insertionSort(unsortedArray))
