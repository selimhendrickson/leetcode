from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S = '', left = 0, right = 0):
            #Check for goal first
            if len(S) == 2 * n:
                ans.append(S)
                # ? Does returning true mean anything here?
                return True
      
            # check constraint
            if left < n:
                # make a choice
                backtrack(S + "(", left + 1, right)
            # check constraint
            if left > right:
                # make a choice
                backtrack(S + ")", left, right + 1)

        backtrack()
        return ans