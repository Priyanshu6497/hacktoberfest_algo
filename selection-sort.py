nums = [64, 25, 12, 22, 11]

for i in range(len(nums)):
    j = i
    min_index = i
    while j < len(nums):
        if nums[j] < nums[min_index]:
            min_index = j
        j += 1
    nums[i], nums[min_index] = nums[min_index], nums[i]
    print("nums after iteration", nums)

print("Final nums :: ", nums)
