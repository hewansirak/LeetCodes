# Last updated: 10/24/2025, 1:43:01 AM
class Solution:
    def decodeString(self, s: str) -> str:

        num_stack = []
        str_stack = []

        curr_num = 0
        curr_str = ''

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)

                curr_num = 0
                curr_str = ''
            elif c == "]":
                num = num_stack.pop()
                prev = str_stack.pop()
                curr_str = prev + curr_str * num
            
            else:
                curr_str += c
        return curr_str

            