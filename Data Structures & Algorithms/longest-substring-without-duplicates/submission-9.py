class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # chars = set()
        # longest = 0
        # l = 0

        # # using hash set
        # for r in range(len(s)):
        #     while s[r] in chars:
        #         chars.remove(s[l])
        #         l += 1

        #     chars.add(s[r])
        #     longest = max(longest, r-l+1)

        # return longest

        chars_map = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if chars_map.get(s[r]) is not None:
                l = max(chars_map[s[r]] + 1, l)
                chars_map[s[r]] = r
            
            chars_map[s[r]] = r
            longest = max(longest, r-l+1)
        return longest




        