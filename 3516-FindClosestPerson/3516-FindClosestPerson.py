# Last updated: 11/20/2025, 10:39:43 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x - z)
        dist2 = abs(y - z)
        
        if dist1 < dist2:
            return 1
        elif dist1 > dist2:
            return 2
        else:
            return 0