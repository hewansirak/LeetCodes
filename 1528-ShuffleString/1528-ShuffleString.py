class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([v for (_,v) in sorted(zip(indices,s))])

        