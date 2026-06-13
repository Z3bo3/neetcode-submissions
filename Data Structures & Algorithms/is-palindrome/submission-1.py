class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        listletters = [letter for letter in s]
        if listletters == listletters[::-1]:
            return True
        return False
        