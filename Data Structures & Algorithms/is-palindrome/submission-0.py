import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        i = 0
        n = len(s)
        j = n-1
        print(s)
        while i<n and i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True

                
        