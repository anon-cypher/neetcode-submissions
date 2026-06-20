class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = {"]":"[", "}":"{", ")":"("}

        if len(s)<2:
            return False
        
        for i in range(len(s)):
            if s[i] in dic.keys() and len(st)>0 and st[-1]==dic[s[i]]:
                st.pop(-1)
            else:
                st.append(s[i])
        
        if len(st)>0:
            return False
        else:
            return True




