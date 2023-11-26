'''
  Problema Palindrome Number do site LeetCode feito em python.
  Link do problema: https://leetcode.com/problems/palindrome-number
'''
class Solution(object):
    def isPalindrome(self, x):
        # Converte o inteiro x em string, pois o código irá funcionar usando string
        s = str(x)
        aux = []
        n = len(s)

        # A lista aux recebe a string invertida do inteiro x
        for i in range(n-1, -1, -1):
            aux.append(s[i])

        # Verifica se o inteiro invertido de x é igual ao inteiro x
        control = True
        for i in range(n):
            if aux[i] != s[i]:
                control = False
                break
            
        return control

x = 121
ret = Solution().isPalindrome(x)
print(ret)
