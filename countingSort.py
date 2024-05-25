def countingSort(arr):
    freq_array = [0] * 100
    
    for num in arr:
        freq_array[num] += 1
    
    return freq_array
