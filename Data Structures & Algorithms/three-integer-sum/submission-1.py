class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        valid_triplets_set = set()
        valid_triplets_lst = []
        for f in range(len(nums)):
            
            # Case 1 :: f == 0, l = 1, r = len-1
            # if f == 0:
            #     l = 1
            #     r = len(nums)-1

            #     while l < r:
            #         if nums[f] + nums[l] + nums[r] == 0:
            #             if tuple(sorted([nums[f], nums[l], nums[r]])) not in valid_triplets_set:
            #                 valid_triplets_lst.append([nums[f], nums[l], nums[r]])
            #             valid_triplets_set.add(tuple(sorted([nums[f], nums[l], nums[r]])))
            #             l += 1
            #             r -= 1
            #         elif nums[f] + nums[l] + nums[r] < 0:
            #             l += 1
            #         elif nums[f] + nums[l] + nums[r] > 0:
            #             r -= 1
            
            # Case 2 :: f = len-1, l = 0, r = f-1 (i.e. len-2)
            # elif f == len(nums)-1:
            #     l = 0
            #     r = len(nums)-2

            #     while l < r:
            #         if nums[f] + nums[l] + nums[r] == 0:
            #             if tuple(sorted([nums[f], nums[l], nums[r]])) not in valid_triplets_set:
            #                 valid_triplets_lst.append([nums[l], nums[r], nums[f]])
            #             valid_triplets_set.add(tuple(sorted([nums[f], nums[l], nums[r]])))
            #             l += 1
            #             r -= 1
            #         elif nums[f] + nums[l] + nums[r] < 0:
            #             l += 1
            #         elif nums[f] + nums[l] + nums[r] > 0:
            #             r -= 1
            
            # Case 3 :: 0 < f < len-1, l = 0, r = len-1
            # else:
            l = 0
            r = len(nums)-1

            while l < r:
                if l == f:
                    l += 1
                elif r == f:
                    r -= 1
                else:
                    if nums[f] + nums[l] + nums[r] == 0:
                        if tuple(sorted([nums[f], nums[l], nums[r]])) not in valid_triplets_set:
                            valid_triplets_lst.append([nums[l], nums[f], nums[r]])
                        valid_triplets_set.add(tuple(sorted([nums[f], nums[l], nums[r]])))
                        l += 1
                        r -= 1
                    elif nums[f] + nums[l] + nums[r] < 0:
                        l += 1
                    elif nums[f] + nums[l] + nums[r] > 0:
                        r -= 1
            
            # print(valid_triplets)
        print(valid_triplets_set)
        return valid_triplets_lst