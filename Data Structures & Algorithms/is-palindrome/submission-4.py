class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l].isalnum() == True and s[r].isalnum() == True: 
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            if s[l].isalnum() == False:
                l += 1
            if s[r].isalnum() == False:
                r -= 1
        return True        

        