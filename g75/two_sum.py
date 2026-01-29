# Dictionary usage reduces time complexity to O(n), instead of nested looping O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, x in enumerate(nums):
            if target - x in my_dict:
                return [my_dict[target - x], i]
            else:
                my_dict[x] = i

    def twoSumLoops(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
