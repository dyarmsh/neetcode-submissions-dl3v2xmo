class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for char in s:
            if char.isalnum():
                cleaned_s += char.lower()
        print(cleaned_s)

        left_ptr = 0
        right_ptr = len(cleaned_s) - 1

        while left_ptr < right_ptr:
            if cleaned_s[left_ptr] != cleaned_s[right_ptr]:
                return False
            left_ptr += 1
            right_ptr -= 1
        return True        

        