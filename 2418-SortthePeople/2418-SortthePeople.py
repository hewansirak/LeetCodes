class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        people = list(zip(heights, names)) 
        
        for i in range(1, n):
            key = people[i]
            j = i - 1

            while j >= 0 and people[j][0] < key[0]:  
                people[j + 1] = people[j]
                j -= 1

            people[j + 1] = key

        return [name for _, name in people]
        