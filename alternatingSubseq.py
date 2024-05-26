def alternating_subsequence(nums):
    result_sum = 0
    curr_max = nums[0]

    for num in nums[1:]:
        if (num > 0 and curr_max > 0) or (num < 0 and curr_max < 0):
            curr_max = max(curr_max, num)
        else:
            result_sum += curr_max
            curr_max = num

    result_sum += curr_max

    return result_sum

t = int(input())  

for _ in range(t):
    n = int(input())  
    nums = list(map(int, input().split()))  # Sequence of elements
    print(alternating_subsequence(nums))
