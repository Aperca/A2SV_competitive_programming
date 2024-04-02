class Solution: 
    def select(self, arr, i):
        minu = i
        for j in range(i+1, len(arr)):
            if arr[minu] > arr[j]:
                minu = j
        return minu
    
    def selectionSort(self, arr, n):
        for i in range(n):
            minu = self.select(arr, i)
            if i != minu:
                arr[minu], arr[i] = arr[i], arr[minu]
