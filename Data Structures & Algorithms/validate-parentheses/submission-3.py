class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) > 1:
            result = []
            CloseToOpen = {")":"(","]":"[","}":"{"}

            for i in s:
                if i in CloseToOpen:
                    if result and result[-1] == CloseToOpen[i]:
                        result.pop()
                    else:
                        return False
                else:
                    result.append(i)
            if len(result) == 0:
                return True 
        return False