from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        intersections = []
        i, j = 0, 0

        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
                continue

            if A[i][0] > B[j][1]:
                j += 1
                continue

            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            intersection = [start, end]            

            intersections.append(intersection)            

            if intersection[1] >= A[i][1]:
                i += 1
            if intersection[1] >= B[j][1]:
                j += 1

        return intersections



        