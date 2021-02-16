class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        mult = 1
        val1, val2 = 0, 0
        
        for i in range(len(num1)-1, -1, -1):
            val1 += int(num1[i]) * mult
            mult = mult * 10
            
        mult = 1
        for i in range(len(num2)-1, -1, -1):
            val1 += int(num2[i]) * mult
            mult = mult * 10
            
        return str(val1 + val2)
            