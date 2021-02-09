from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        tuples = [[x, y] for x, y in count.items()]
        tuples.sort(key = lambda x: x[1], reverse=True)
        chars = [t[0] * t[1] for t in tuples]  
        return "".join(chars)        