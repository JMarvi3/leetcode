class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        end = min(len(s) for s in strs)
        for i in range(end):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return strs[j][:i]
        return strs[0][:end]