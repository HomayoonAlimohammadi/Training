from typing import List 


class Interval:
    '''Time intervals for staff meetings'''
    def __init__(self, start: int, end: int) -> None:
        self.start = start 
        self.end = end 

    def __str__(self):
        return f'Interval{{start: {self.start}, end: {self.end}}}'
    
    def __repr__(self):
        return f'Interval({self.start}, {self.end})'


def insert_interval(meetings: List[Interval], duration: int) -> Interval:
    if meetings[0].start > duration:
        return Interval(0, duration)

    for i in range(len(meetings) - 1):
        if meetings[i].end + 1 + duration < meetings[i+1].start:
            return Interval(meetings[i].end + 1, meetings[i].end + 1 + duration)
    
    return Interval(meetings[-1].end + 1, meetings[-1].end + 1 + duration)

def main() -> None:
    meetings: List[Interval] = []
    
    n_lines = int(input())
    for i in range(n_lines):
        idx, start, end = input().split()
        interval = Interval(int(start), int(end))
        meetings.append(interval)

    meetings.sort(key = lambda interval: interval.start)
    idx, new_meeting_duration = input().split()
    new_meeting_duration = int(new_meeting_duration)

    new_interval = insert_interval(meetings, new_meeting_duration)
    print(new_interval.start, new_interval.end)


if __name__ == '__main__':
    main()