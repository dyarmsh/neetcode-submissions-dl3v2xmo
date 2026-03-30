class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:  # O(n)
            frequencies[num] += 1

        counts = [[] for _ in range(len(nums))]

        for num, freq in frequencies.items(): # O(n)
            counts[freq - 1].append(num)
        
        res = []
        i = len(counts)
        while len(res) < k and i >= 0:
            if len(counts[i-1]) > 0:
                for elem in counts[i-1]: # O(n)
                    res.append(elem)
            i -= 1

        return(res)
            