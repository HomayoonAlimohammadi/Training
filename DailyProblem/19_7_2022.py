from typing import List, Union
import bisect


def compute_running_median(nums: List[Union[int, float]]) -> None:
    nums_flow = []
    for num in nums:
        bisect.insort(nums_flow, num)
        len_flow = len(nums_flow)
        if len(nums_flow[:len_flow]) % 2 != 0:
            print(nums_flow[len_flow // 2])
        else:
            print((nums_flow[len_flow // 2] + nums_flow[len_flow // 2 - 1]) / 2)


nums = [2, 1, 5, 7, 2, 0, 5]
compute_running_median(nums)
