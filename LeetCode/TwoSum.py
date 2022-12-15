class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for x in range(len(nums)):
            for i in range(x+1,len(nums)):
                if nums[i]+nums[x]==target:
                    output.append(i)
                    output.append(x)
                    return output
nums = input()