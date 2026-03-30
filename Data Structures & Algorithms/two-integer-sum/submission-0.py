class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            
            if nums_dict.get(nums[i]) is not None:
                return [nums_dict.get(nums[i]), i]
                
            nums_dict[target - nums[i]] = i
        