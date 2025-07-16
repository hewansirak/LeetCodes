# Last updated: 7/16/2025, 11:18:55 PM
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        
        five = 0
        ten = 0

        for x in bills:
            if x == 5:
                five += 1
            elif x == 10:
                if five > 0:
                    five -= 1
                else:
                    return False
                ten += 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five > 2 :
                    five -= 3
                else:
                    return False
            print(five, ten)
        return True