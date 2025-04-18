#Approach 1: Brute Force 
#        for i in range(len(nums) - 1):
#            for j in range(i+1, len(nums)):
#                if nums[i] + nums[j] == target:
#                    return([i,j])
#TC: O(n^2)

#Approach 2: Dictionary Method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     seen = {}
     for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        elif num not in seen:
            seen[num] = i

#TC: O(n)
