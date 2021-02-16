from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charmap = {}

        # build a map to lookup the order
        for i in range(len(order)):
            charmap[order[i]] = i

        for j in range(len(words)-1):
            word1 = words[j]
            word2 = words[j+1]

            for k in range(len(word1)):
                # first word is longer so ordering is correct, move to the next combination of words
                if k == len(word2): return False
                if charmap[word1[k]] < charmap[word2[k]]: break
                elif charmap[word1[k]] > charmap[word2[k]]: return False

        # if we reach here, list of words is sorted
        return True        
