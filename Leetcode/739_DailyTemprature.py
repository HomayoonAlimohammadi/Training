from typing import List


### Brute Force!

class Solution1:

    def dailyTemperature(self, temperatures: List[int]) -> List[int]:

        sorted_temp = sorted(temperatures)
        if temperatures == sorted_temp:
            return [1] * (len(temperatures)-1) + [0]
        elif temperatures == sorted_temp[::-1]:
            return [0] * len(temperatures)

        days = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            wait = 0
            for j in range(i+1, len(temperatures)):
                wait += 1
                if temperatures[j] > temp:
                    break
            else:
                wait = 0
            days.append(wait)

        return days


### One pass

class Solution2:

    def dailyTemperature(self, temperatures: List[int]) -> List[int]:

        days = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            while stack and current_temp > stack[-1][0]:
                last_temp, last_day = stack.pop()
                days[last_day] = i - last_day

            record = (current_temp, i)
            stack.append(record)

        return days


sol = Solution2()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperature(temperatures))