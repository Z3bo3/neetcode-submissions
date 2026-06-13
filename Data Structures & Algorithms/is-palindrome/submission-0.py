class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").replace("?", "").replace("!", "").replace(",", "").replace("'", "").replace(".", "").replace(":", "")
        s = s.lower()
        listletters = [letter for letter in s]
        if listletters == listletters[::-1]:
            return True
        return False
        