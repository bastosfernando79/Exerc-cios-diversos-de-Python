'''
  Problema Roman to Integer do site LeetCode. Feito em python.
  link do problema: https://leetcode.com/problems/roman-to-integer
'''
class Solution(object):
    def romanToInt(self, s):
        # Coloca toda a string s com letras maiúsculas, caso o usuário coloque em minúsculas
        su = s.upper() 
        
        # Dicionário  
        roman_values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        # Retorna o dígito de cada letra correspondente. Ex: 'X' retorna 10.
        def convertToInt(su):
            return roman_values[su]

        # Usa o map para criar uma lista de cada um dos valores correspondentes. Ex: 'XXI' retorna [10, 10, 1]
        values = list(map(convertToInt, su))  
        decimal = 0
        
        for i in range(len(values) - 1):
            if values[i] < values[i+1]:
                decimal -= values[i]
            else:
                decimal += values[i]
        
        decimal += values[-1]        
        
        return decimal
    
s = "XxIi"
ans = Solution().romanToInt(s)
print(ans)
