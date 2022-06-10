from typing import List 


class Interval:
    '''Time intervals for staff meetings'''

    def __init__(self, start: int, end: int) -> None:
        self.start = start 
        self.end = end 
        self.duration = end - start

    def __str__(self):
        return f'Interval{{start: {self.start}, end: {self.end}}}'
    
    def __repr__(self):
        return f'Interval({self.start}, {self.end})'


class Calendar:
    '''Calendar class for managing staff meetings and schedules.'''
    
    def calculate_overlap(self, interval_1: Interval, interval_2: Interval) -> int:
        '''Calcualte overlap between two instances of Interval in epochs'''

        # make sure interval_1 start is before interval_2 start
        if interval_1.start > interval_2.start: 
            interval_1, interval_2 = interval_2, interval_1
        
        # no overlap
        if interval_2.start > interval_1.end: 
            return 0

        # interval_2 inside interval_1
        if interval_2.end < interval_1.end: 
            return interval_2.end - interval_2.start

        return interval_1.end - interval_2.start

    def get_inputs(self) -> List[Interval]:
        '''
        First, retrieves `n` as the number of meetings of a staff.
        After that, retrieves `n` lines each one describing
        one of the corresponding staff's meetings.
        Return the staff's schedule afterwards.
        '''
        n = int(input())
        n_intervals = []
        for i in range(n):
            idx, start, end = input().split()
            start, end = int(start), int(end)
            n_intervals.append(Interval(start, end))

        return n_intervals

    def calculate_total_overlap(self, schedule_1: List[Interval], \
                                      schedule_2: List[Interval]) -> int:
        '''
        Calculate total overlap of same meetings between 
        two employee's schedules.
        '''
        total_overlap = 0
        n_common = min(len(schedule_1), len(schedule_2))
        for i in range(n_common):
            interval_1 = schedule_1[i]
            interval_2 = schedule_2[i]
            total_overlap += self.calculate_overlap(interval_1, interval_2)

        return total_overlap


def client(calendar: Calendar) -> None:

    calendar = Calendar()
    first_employee_schedule = calendar.get_inputs()
    second_employee_schedule = calendar.get_inputs() 

    overlap = calendar.calculate_total_overlap(
        first_employee_schedule,
        second_employee_schedule
    )

    print(overlap)

if __name__ == '__main__':
    calendar = Calendar()
    client(calendar)

