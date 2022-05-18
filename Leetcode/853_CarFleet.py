from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        records = [
            (pos, spd) for pos, spd in zip(position, speed)
        ]
        
        records.sort(key=lambda x: x[0])
        
        for i in range(len(records)):
            records[i] = (target - records[i][0])/records[i][1]
            
        stack = []
        for record in records:
            while stack and record >= stack[-1]:
                stack.pop()
                
            stack.append(record)
        
        return len(stack)