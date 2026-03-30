class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dicts = []
        anagrams_lst = []
        for index, word in enumerate(strs): # O(#total chars)
            word_dict = {}

            for char in word:
                word_dict[char] = word_dict.get(char, 0) + 1
            
            if index == 0:
                anagrams_lst.append([strs[index]])
                word_dicts.append(word_dict)
            else:
                if word_dict in word_dicts:
                    if word_dicts.index(word_dict) >= len(anagrams_lst):
                        anagrams_lst.insert(word_dicts.index(word_dict),[word])
                    else:
                        anagrams_lst[word_dicts.index(word_dict)].append(word)
                        
                else:
                    word_dicts.append(word_dict)
                    anagrams_lst.insert(word_dicts.index(word_dict),[word])
        
        return anagrams_lst
        