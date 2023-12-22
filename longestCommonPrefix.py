'''
  Problema Longest Common Prefix do site LeetCode feito em python.
  Link do problema: https://leetcode.com/problems/longest-common-prefix/
'''
class Solution(object):
    def longestCommonPrefix(self, strs):        
        if not strs:
            return ""

        # Ordena as strings para garantir que a comparação seja feita corretamente
        strs.sort()

        # Pega o primeiro e último elemento (os mais diferentes)
        first_str = strs[0]
        last_str = strs[-1]

        prefix = []
        
        # Encontra o prefixo comum entre o primeiro e o último elemento
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                prefix.append(first_str[i])
            else:
                break

        return "".join(prefix)    

strs = ["flower","flow","flight"]
ret = Solution().longestCommonPrefix(strs)
print(ret)
