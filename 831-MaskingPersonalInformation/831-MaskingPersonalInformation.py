# Last updated: 9/18/2025, 11:43:16 PM
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            d = ['*','*','*','*','*','*','*']

            s = s.lower()

            email = re.split("@",s)
            d[0] = email[0][0]
            d[6] = email[0][-1]
            d = ''.join(d)
            return(d + '@' + email[1])
        s = re.split("[-|+|, |()|' ']", s)
        s = ''.join(s)
        
        if s.isdigit():
            if len(s) == 10:
                return('***-***-' + s[6:10])
            elif len(s) == 11:
                return('+*-***-***-' + s[7:11])
            elif len(s) == 12:
                return('+**-***-***-' + s[8:12])
            elif len(s) == 13:
                return('+***-***-***-' + s[9:13])