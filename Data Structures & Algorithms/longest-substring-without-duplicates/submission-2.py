class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = set()
        l = 0
        counter = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            counter = max(counter, r-l+1)
        return counter


"dvdf"