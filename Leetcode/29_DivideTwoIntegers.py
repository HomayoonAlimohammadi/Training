##### My Solution! Time Limit Exceeded!
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(dividend) == dividend:
            dividend_sign = True
        else:
            dividend_sign = False
        if abs(divisor) == divisor:
            divisor_sign = True
        else:
            divisor_sign = False
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        if divisor != 1:
            result = 0
            while dividend >= divisor:
                dividend -= divisor
                result += 1
        else:
            result = dividend
            
        if dividend_sign ^ divisor_sign:
            result *= -1
            
        if result <= -2**31:
            result = -2**31
        elif result >= (2**31 - 1):
            result = 2**31 - 1
        return result
    
S = Solution()
print(S.divide(-2147483648,1))
            
        
        

#### Solution:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return None
        diff_sign = (divisor<0) ^ (dividend<0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        max_divisor = divisor
        shift_count = 1
        while dividend >= (max_divisor << 1):
            max_divisor <<= 1
            shift_count <<= 1
        
        while shift_count >= 1:
            if dividend >= max_divisor:
                dividend -= max_divisor
                result += shift_count
            shift_count >>= 1
            max_divisor >>= 1
            
        if diff_sign:
            result = -result
        return max(min(result, 2**31 - 1), -2**31)