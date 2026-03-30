class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        max_length = 0

        for num in nums: 

            # finding first element in sequence
            if num-1 not in nums: # O(1)
                seq_length = 1
                while num+seq_length in nums:
                    seq_length+=1

                max_length = max(max_length, seq_length)
        
        return max_length
