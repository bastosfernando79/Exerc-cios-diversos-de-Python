class Solution(object):
    def isValid(self, s):
        # Esse algorítmo utiliza a Estrutura de Dados Pilha
        pilha = []

        # Dicionário
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # Caso seja open ela se junta a pilha
            if char in mapping.values():
                pilha.append(char)
            elif char in mapping.keys():
                if not pilha or pilha.pop() != mapping[char]:
                    return False
            # Caso seja dada algum outro caractere diferente do pedido
            else:
                return False

        # not pilha retorna False por padrão, só retorna True se ela for vazia
        return not pilha

s = "({})"
ret = Solution().isValid(s)
print(ret)      
