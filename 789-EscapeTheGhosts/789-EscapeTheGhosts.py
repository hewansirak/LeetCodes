# Last updated: 8/6/2025, 11:33:49 PM
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        steps = abs(0 - target[0]) + abs(0 - target[1])
        
        for ghost in ghosts:
            ghoststep = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
        
            if ghoststep <= steps:
                return False
        
        return True
        