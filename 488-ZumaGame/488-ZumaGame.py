# Last updated: 11/30/2025, 10:40:21 PM
1class Solution:
2    def findMinStep(self, board: str, hand: str) -> int:
3        
4        def remove_same(s, i):
5            if i < 0:
6                return s
7            
8            left = right = i
9            while left > 0 and s[left-1] == s[i]:
10                left -= 1
11            while right+1 < len(s) and s[right+1] == s[i]:
12                right += 1
13            
14            length = right - left + 1
15            if length >= 3:
16                new_s = s[:left] + s[right+1:]
17                return remove_same(new_s, left-1)
18            else:
19                return s
20
21        hand = "".join(sorted(hand))
22
23        q = collections.deque([(board, hand, 0)])
24        visited = set([(board, hand)])
25
26        while q:
27
28            curr_board, curr_hand, step = q.popleft()
29            for i in range(len(curr_board)+1):
30                for j in range(len(curr_hand)):
31                    if j > 0 and curr_hand[j] == curr_hand[j-1]:
32                        continue
33                    
34                    if i > 0 and curr_board[i-1] == curr_hand[j]:
35                        continue
36                    
37                    pick = False
38
39                    if i < len(curr_board) and curr_board[i] == curr_hand[j]:
40                        pick = True
41                    if 0<i<len(curr_board) and curr_board[i-1] == curr_board[i] and curr_board[i] != curr_hand[j]:
42                        pick = True
43                    
44                    if pick:
45                        new_board = remove_same(curr_board[:i] + curr_hand[j] + curr_board[i:], i)
46                        new_hand = curr_hand[:j] + curr_hand[j+1:]
47                        if not new_board:
48                            return step + 1
49                        if (new_board, new_hand) not in visited:
50                            q.append((new_board, new_hand, step+1))
51                            visited.add((new_board, new_hand))
52
53        return -1