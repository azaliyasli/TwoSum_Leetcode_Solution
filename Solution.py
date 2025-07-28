class Solution(object):
    
    def twoSum(self, nums, target):
        indices = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices:
                return [indices[diff], i]
            else:
                indices[nums[i]] = i
