from typing import Dict, List 


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


class Employee:
    '''Employee class for managing staff id and schedules.'''

    def __init__(self, user_id: int, busy_day: str = None, 
                 meetings: Dict[str, List[Interval]] = {}):
        self.user_id = user_id 
        self.busy_day = busy_day 
        self.meetings = meetings 

    def __str__(self):
        f'User #{self.user_id}'


class Calendar:
    '''Calendar class for managing staff meetings and schedules.'''

    def __init__(self, n_users: int, users_meetings: Dict[str, List[Interval]] = {},
                 busy_days: set = set(), ) -> None:
        self.busy_days = busy_days
        self.users_meetings = users_meetings
        self.n_users = n_users
        self.days = ['MONDAY', 'TUESDAY', 'WEDNESDAY',
                    'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    def get_employee(self) -> List[Interval]:
        '''
        First retrieves `user_id` and `busy_day` for a staff.
        Then, retrieves `n` as the number of meetings of the staff.
        After that, retrieves `n` lines each one describing
        one of the corresponding staff's meetings.
        Return employee instance 
        '''


        n = int(input())
        n_intervals = []
        for i in range(n):
            idx, start, end = input().split()
            start, end = int(start), int(end)
            n_intervals.append(Interval(start, end))

        return n_intervals

    def merge(self, intervals: List[Interval]) -> List[Interval]:
        '''
        Merge overlapping intervals inside a list of intervals
        Return updated list of intervals.
        '''

        intervals.sort(key = lambda x: x.start)
        n_s = []
        i = 0
        while i < len(intervals):
            inter = intervals[i]
            while i < len(intervals) - 1 and inter.end >= intervals[i+1].start:
                i += 1
                inter.end = max(inter.end, intervals[i].end)
                
            n_s.append(inter)
            i += 1

        return n_s

    def insert_merge(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        '''
        Insert a new interval inside a list of non-overlapping intervals.
        Merge resulted list of intervals if needed (hence the name "insert_merge").
        '''

        if len(intervals) == 0:
            return [newInterval]
        i = 0
        while i < len(intervals) and intervals[i].start < newInterval.start:
            i += 1
        intervals.insert(i, newInterval)
        intervals = self.merge(intervals)

        return intervals

    def put_interval(self, intervals: List[Interval], duration: int) -> Interval:
        '''
        Pick and Return earliest time interval given it's duration regarding the list of 
        current intervals. 
        '''

        if intervals[0].start > duration:
            return Interval(0, duration)

        for i in range(len(intervals)-1):
            if intervals[i].end + 1 + duration < intervals[i+1].start:
                return Interval(intervals[i].end + 1,
                                intervals[i].end + 1 + duration)
            
        return Interval(intervals[-1].end + 1, intervals[-1].end + 1 + duration)


def client(calendar: Calendar):
    '''
    Client takes the company's calendar. 
    Retrieve user data in accordance with `calendar.n_users`
    Update calendar correspondingly.
    Handles new meeting timestamp.
    '''

    for i in range(calendar.n_users):
        user_id = int(input())
        calendar.busy_days.add(input())
        
        n_meetings = int(input())
        for j in range(n_meetings):
            idx, day, start, end = input().split()
            start, end = int(start), int(end)
            meetings = calendar.users_meetings.get(day, [])
            calendar.users_meetings[day] = \
                calendar.insert_merge(meetings, Interval(start, end))

    idx, duration = input().split()
    duration = int(duration)

    for day in calendar.days:
        if day in calendar.busy_days:
            continue 
        
        intervals = calendar.users_meetings[day]
        new_interval = calendar.put_interval(intervals, duration)

        # Check to see if the meeting is in day time boundry.
        if new_interval.end <= 32400000:
            print(day, new_interval.start, new_interval.end)
            break 

if __name__ == '__main__':
    n_users = int(input())
    calendar = Calendar(n_users)
    client(calendar)