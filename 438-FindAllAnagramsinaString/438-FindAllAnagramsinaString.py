# Last updated: 4/11/2025, 9:37:09 PM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_init = set(p)
        p_dict = dict()

        for char in p:
            if p_dict.get(char, None) is None:
                p_dict[char] = 1
            else:
                p_dict[char] += 1

        if len(p) > len(s):
            return result

        for i in range(len(p)):
            if s[i] in p_init:
                if p_dict.get(s[i], None) is not None:
                    p_dict[s[i]] -= 1
                    if p_dict[s[i]] == 0:
                        del p_dict[s[i]]
                else:
                    p_dict[s[i]] = -1

        if not p_dict:
            result.append(0)

        for i in range(len(p), len(s)):
            if s[i - len(p)] in p_init:
                if p_dict.get(s[i - len(p)], None) is not None:
                    p_dict[s[i - len(p)]] += 1
                    if p_dict[s[i - len(p)]] == 0:
                        del p_dict[s[i - len(p)]]
                else:
                    p_dict[s[i - len(p)]] = 1

            if s[i] in p_init:
                if p_dict.get(s[i], None) is not None:
                    p_dict[s[i]] -= 1
                    if p_dict[s[i]] == 0:
                        del p_dict[s[i]]
                else:
                    p_dict[s[i]] = -1
            if not p_dict:
                result.append(i - len(p) + 1)

        return result