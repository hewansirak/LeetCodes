# Last updated: 11/7/2025, 11:38:23 PM
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        onetotwnety = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def threeDigits(n):
            if n == 0:
                return ""
            elif n < 20:
                return onetotwnety[n]
            elif n < 100:
                return tens[n // 10] + (" " + onetotwnety[n % 10] if n % 10 != 0 else "")
            else:
                return onetotwnety[n // 100] + " Hundred" + (" " + threeDigits(n % 100) if n % 100 != 0 else "")

        result = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                result = threeDigits(num % 1000) + (" " + thousands[i] if thousands[i] else "") + (" " + result if result else "")
            num //= 1000
            i += 1

        return result.strip()
