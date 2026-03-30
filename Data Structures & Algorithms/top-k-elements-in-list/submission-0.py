class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        
        for num in nums: # O(n)
            frequencies[num] += 1

        # O(nlogn)
        lst = (sorted(frequencies.items(), key=lambda freq: freq[1], reverse = True ))

        return [x[0] for x in lst[:k]] # O(n)
        