class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        people = list(zip(heights, names)) 
        
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if people[j] < people[j + 1]:
                    people[j], people[j + 1] = people[j + 1], people[j]  
                    swapped = True

        return [name for _, name in people]
        