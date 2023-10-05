# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.


def twoSum(nums, target):
    if nums == []:
        return None
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


lst = [2, 7, 11, 15]
target = 9
print(twoSum(lst, target))
