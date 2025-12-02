# Last updated: 12/2/2025, 10:20:25 PM
1class Twitter:
2
3    def __init__(self):
4        self.count = 0
5        self.tweetMap = defaultdict(list) #list of [count, tweetId]
6        self.followMap = defaultdict(set) #set of followeeId        
7
8    def postTweet(self, userId: int, tweetId: int) -> None:
9        self.tweetMap[userId].append([self.count, tweetId])
10        self.count -= 1
11
12    def getNewsFeed(self, userId: int) -> List[int]:
13        res = [] 
14        minHeap = []
15
16        self.followMap[userId].add(userId)
17        for followeeId in self.followMap[userId]:
18
19            if followeeId in self.tweetMap:
20                index = len(self.tweetMap[followeeId]) - 1
21                count, tweetId = self.tweetMap[followeeId][index]
22                minHeap.append([count, tweetId, followeeId, index - 1])
23        
24        heapq.heapify(minHeap)
25
26        while minHeap and len(res) < 10:
27            count, tweetId, followeeId, index = heapq.heappop(minHeap)
28            res.append(tweetId)
29
30            if index >= 0:
31                count, tweetId = self.tweetMap[followeeId][index]
32                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
33        
34        return res
35
36    def follow(self, followerId: int, followeeId: int) -> None:
37        self.followMap[followerId].add(followeeId)        
38
39    def unfollow(self, followerId: int, followeeId: int) -> None:
40        if followeeId in self.followMap[followerId]:
41            self.followMap[followerId].remove(followeeId)
42        
43
44
45# Your Twitter object will be instantiated and called as such:
46# obj = Twitter()
47# obj.postTweet(userId,tweetId)
48# param_2 = obj.getNewsFeed(userId)
49# obj.follow(followerId,followeeId)
50# obj.unfollow(followerId,followeeId)