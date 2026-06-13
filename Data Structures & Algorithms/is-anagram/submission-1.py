class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = [letter for letter in s]
        listt = [letter for letter in t]
        if sorted(lists) == sorted(listt):
            return True
        return False

        