class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list) # at most O(m)

        for word in strs: # O(m)
            char_freq = [0] * 26
            for char in word: # O(n)
                char_freq[ord(char) - ord("a")] += 1

            anagrams[tuple(char_freq)].append(word) # using tuple as key as it is immutable
            
        return list(anagrams.values())
        