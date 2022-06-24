"""
Given the mapping from A-Z being 1-27,
calculate number of the ways which a string
can be decoded.
- Presume that the given string is decodable.
"""
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def calculate_ways(code: str):
            """
            Return number of the decoding ways.
            Cache is used to reduce redundancy
            """
            if not code:
                return 1

            if code[0] == "0":
                return 0

            if len(code) == 1:
                return 1

            total = calculate_ways(code[1:])
            if int(code[:2]) in range(10, 27):
                total += calculate_ways(code[2:])

            return total

        return calculate_ways(s)
