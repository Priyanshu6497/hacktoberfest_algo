nums = [2, 5, 7, 8, 1, 3, 4]

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print("nums after ${i} iteration", nums)

print("Final nums :: ", nums)
