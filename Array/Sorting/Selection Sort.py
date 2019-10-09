
class Solution:
    def selectionSort(self, arr):
        arrayLength = len(arr)

        for i in range(arrayLength):
            minimumIndex = i
            for j in range(i+1, arrayLength - 1):
                if (arr[j] < arr[minimumIndex]):
                    minimumIndex = j
            temp = arr[minimumIndex]
            arr[minimumIndex] = arr[i]
            arr[i] = temp

        return arr


if __name__ == "__main__":
    unsortedArray = [64, 34, 25, 12, 22, 11, 90]
    print("The sorted array is")
    print(Solution().selectionSort(unsortedArray))
