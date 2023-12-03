""" 
  Problema Minimum Time Visiting All Points do site LeetCode feito em python.
  Link do problema: https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2023-12-03
"""
# Função que calcula a distância entre dois pontos diferentes
def maxDifference(x, y):
        xi = abs(x[0] - y[0])
        yi = abs(x[1] - y[1])

        if xi >= yi:
            return xi
        else: 
            return yi

class Solution(object):    
    def minTimeToVisitAllPoints(self, points):    
        # Contador da distância entre dois pontos  
        count = 0
        # Loop que passa por cada um dos pontos 
        for i in range(1, len(points)):
            distance = maxDifference(points[i-1], points[i])
            count = count + distance

        return count 

points = [[1,1],[3,4],[-1,0]]
ret = Solution().minTimeToVisitAllPoints(points)
print(ret)        
