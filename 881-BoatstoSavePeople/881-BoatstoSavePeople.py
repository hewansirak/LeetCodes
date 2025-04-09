# Last updated: 4/9/2025, 10:58:18 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        x = 0
        l, r = 0, len(people)-1
        while l <= r:
            x +=1
            if people[l] + people[r] <= limit:
                l +=1
            r -=1
        return x