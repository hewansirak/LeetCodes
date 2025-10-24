# Last updated: 10/24/2025, 11:53:12 AM
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        result = val not in self.numMap
        if result:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return result        

    def remove(self, val: int) -> bool:
        result = val in self.numMap
        if result:
            idx = self.numMap[val]
            lastval = self.numList[-1]
            self.numList[idx] = lastval
            self.numList.pop()
            self.numMap[lastval] = idx
            del self.numMap[val]
        return result
    
    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()