'''
  Problema Roman to Integer do site LeetCode feito em python.
  https://leetcode.com/problems/roman-to-integer
'''
class Solution(object):
    def romanToInt(self, s):
      # Definindo um dicionário 
      valores_romanos = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
        # Diz o dígito de cada letra correspondente. Ex: 'X' retorna 10.
        def convertToInt(s):
            return valores_romanos[s]

        # Usa o map para criar uma lista de cada um dos valores correspondentes. Ex: 'XXI' retorna [10, 10, 1]
        valores = list(map(convertToInt, s))  
        decimal = 0
        
        for i in range(len(valores) - 1):
            if valores[i] < valores[i+1]:
                decimal -= valores[i]
            else:
                decimal += valores[i]
        
        decimal += valores[-1]        
        
        return decimal
