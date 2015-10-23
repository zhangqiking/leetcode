class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp=strs[0]
        com=[]
        for s in strs:
            if len(s)<len(temp):
                temp=s
        for i in range(len(temp)):
            for s in strs:
                if (s[i]!=temp[i]):
                    return com
            com.append(temp[i])
        return com
s=Solution()
print s.longestCommonPrefix(["abgtb","abt","abjir"])
