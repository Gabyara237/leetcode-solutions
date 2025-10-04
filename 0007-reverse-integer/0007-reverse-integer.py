class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign= -1
        else:
            sign=1
        x = abs(x)

        result=0
        range_max= 2**31-1
        range_min= -2**31

        while x!=0:
            digit= x % 10
            x=x//10
            if result> range_max//10:
                return 0
            if result== range_max //10 and digit>7:
                return 0

            result=result *10 + digit

        return sign*result