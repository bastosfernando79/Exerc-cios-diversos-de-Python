""" 
  Problema Sort_Integers_by_the_Number_of_Bits do site LeetCode feito em python.
  Link do problema: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""
# Converte o número para binário e depois conta o número de dígitos 1 desse binário
def count_1(x):
    binary = bin(x)
    count = binary.count('1')
    return count
    
class Solution(object):
    def sortByBits(self, arr):
        # Cria 15 listas vazias para cada uma das opções (uso do ChatGPT)
        lista = {}
        for i in range(0, 15):
            lista[i] = []
        
        # Coloca cada número em sua respectiva lista
        for i in range(len(arr)):
            for j in range(15):  
                if (count_1(arr[i])) == j:
                    lista[j].append(arr[i])        
        
        # Coloca tudo numa só lista e já ordena os elementos de cada uma das listas (usando a função sorted)
        final_list = []
        for i in range(0, 15):
            final_list = final_list + sorted(lista[i])
    
        return final_list

arr = [2,3,5,7,11,13,17,19]
ret = Solution().sortByBits(arr)
print(ret)        
