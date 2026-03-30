class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6] -> [48,24,12,8]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        result = [0] * len(nums)

        pref[0] = 1
        suff[len(nums)-1] = 1

        for i in range(1, len(nums)):
            pref[i] = nums[i-1] * pref[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]

        print(pref)
        print(suff)

        for i in range(len(nums)):
            result[i] = pref[i] * suff[i]


        return result

        