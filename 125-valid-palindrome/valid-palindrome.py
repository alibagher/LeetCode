class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
                newS += c.lower()

        i = 0
        j = len(newS) - 1
        for c in newS:
            if i == j:
                break
            if newS[i] != newS[j]:
                return False
            i += 1
            j -= 1
        return True