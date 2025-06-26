# Last updated: 6/26/2025, 10:42:20 PM
class Solution:
    def lexicalOrder(self, target: int) -> List[int]:
        def dfs(curr):
            if curr > target:
                return 
            ans.append(curr)
            for next_digit in range(10):
                generated_num = curr * 10 + next_digit
                
                if generated_num > target:
                    return 

                dfs(generated_num)
        ans = []
        for start in range(1, 10):
            dfs(start)
        return ans
            

