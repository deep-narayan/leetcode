class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(0,len(haystack)) :
            if (haystack[i] == needle[0]) and (haystack[i:i+len(needle)] == needle):
                return i
            
        else:
            return -1

        