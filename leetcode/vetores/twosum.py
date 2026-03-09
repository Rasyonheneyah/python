# Estratégia:
# 1. Criar uma tabela hash para mapear numero -> indice
# 2. Para cada numero, calcular o complemento (target - numero)
# 3. Verificar se esse complemento existe na tabela
# Complexidade: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        tabelaHash = {}

        # cria uma tabela hash que mapeia numero -> indice
        for i in range(n):
            tabelaHash[nums[i]] = i

        # percorre o array procurando o complemento que soma ao target
        for i in range(0, n-1):
            # verifica se o complemento existe e se não é o mesmo elemento
            j = target - nums[i]
            if j in tabelaHash and i!= tabelaHash[j]:
                return [i, tabelaHash[j]]
            
            
            
         
# Testes 

s = Solution()

print(s.twoSum([2,7,11,15], 9))   # esperado: [0,1]
print(s.twoSum([3,2,4], 6))       # esperado: [1,2]
print(s.twoSum([3,3], 6))         # esperado: [0,1]