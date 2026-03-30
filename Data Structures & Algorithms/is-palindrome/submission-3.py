class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaned_s = ""
        # for char in s:
        #     if char.isalnum():
        #         cleaned_s += char.lower()
        # print(cleaned_s)

        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            if s[left_ptr].isalnum() == True and s[right_ptr].isalnum() == True: 
                if s[left_ptr].lower() != s[right_ptr].lower():
                    return False
                left_ptr += 1
                right_ptr -= 1
            if s[left_ptr].isalnum() == False:
                left_ptr += 1
            if s[right_ptr].isalnum() == False:
                right_ptr -= 1
        return True        

        