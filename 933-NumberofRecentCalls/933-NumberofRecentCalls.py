# Last updated: 5/21/2025, 10:25:50 PM
class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        start, end = 0, len(self.pings) - 1
        while end > start:
            mid = (start+end)//2
            if self.pings[mid] < t - 3000:
                start = mid + 1
            else:
                end = mid
        start = start + 1 if self.pings[start] < t - 3000 else start

        return len(self.pings) - start
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)