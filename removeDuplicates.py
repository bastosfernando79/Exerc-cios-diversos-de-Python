'''
  Problema Remove Duplicates from Sorted Array do site LeetCode. Feito em python.
  link do problema: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''
def removeDuplicates(nums):
    # Verifica se a lista possui algum elemento
    if not nums:
        return 0

    # Contador de elementos únicos
    k = 1  
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

nums = [1, 1, 2]
expectedNums = [1, 2]
k = removeDuplicates(nums)

# Verificação do Custom Judge
assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]

print(f"Output: {k}, nums = {nums[:k]}")
