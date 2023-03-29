class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s)== 0:
            return 0
        visited = set()
        left, maxLen = 0, 0
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[i])
            currLen = i-left + 1
            maxLen = max(maxLen, currLen)
        return maxLen