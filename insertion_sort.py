def insertion_sort(nums):
    for i in range(1, len(nums)):
        cur_value = nums[i]
        k = i
        while k > 0 and cur_value < nums[k - 1]:
            nums[k] = nums[k - 1]
            k -= 1
        nums[k] = cur_value
    return nums


numbs = [1, 2, 3, 4, 5, 6]
print(insertion_sort(numbs))
