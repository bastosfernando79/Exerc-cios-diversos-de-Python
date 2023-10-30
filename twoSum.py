'''
  Problema twoSum do site LeetCode feito em python
  Link do problema: https://leetcode.com/problems/two-sum
'''
class Solution(object):
    def twoSum(self, nums, target):
        size = len(nums)
        boolean = False
        x1 = 0
        x2 = 0
                
        for i in range(size):
            for j in range(i+1, size):
                aux = nums[i] + nums[j]
                if aux == target:
                    x1 = i
                    x2 = j
                    boolean = True
            if boolean == True:
                break

        lista = [x1, x2]
        return lista

nums = [2,4,11,3]
target = 6
ret = Solution().twoSum(nums, target)
print(ret)
    
    
    
