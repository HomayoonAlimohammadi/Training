'''
calendar module designed to be used in CarWash instances
'''

from typing import List, Tuple
from utils import ReservationTicket


class Calendar:
    '''Calendar class for keeping track of reserved times in CarWash.'''

    def __init__(self, n_months: int = 1, n_days: int = 30) -> None:
        '''
        Initialize Calendar with the time span of 1 month(s).
        Each month is 30 days.
        '''
        self._minutes_per_day = 24 * 60
        self._days = n_days
        self._months = n_months
        self._calendar: List[List[int]]
        self._setup_calendar()

    def _setup_calendar(self) -> None:
        '''
        Set up calendar with corresponding `months` and `days`.
        '''
        self._calendar = []
        for mo in range(self._months):
            month = []
            for d in range(self._days):
                day = [0 for _ in range(self._minutes_per_day)]
                month.append(day)
            self._calendar.append(month)

    def get_day(self, month: int, day: int) -> List[int]:
        '''Get a specific day of a specific month.'''
        if not isinstance(month, int) or not isinstance(day, int):
            raise ValueError(f'Day ({day}) and Month ({month}) should be both integers.')
        if month not in range(1,self._months+1) or day not in range(1,self._days+1):
            raise ValueError(f'Day ({day}) or Month ({month}) does not exist in the calendar')

        return self._calendar[month-1][day-1]

    def fill_earliest(self, ticket: ReservationTicket) -> dict:
        '''Fill the earliest time available according to the ticket'''
        raise NotImplementedError

    def fill_specific(self, ticket: ReservationTicket, time: Tuple[int, int]) -> dict:
        '''Fill the specific time if possible'''
        raise NotImplementedError

    def __str__(self) -> None:
        result = ''
        for mo in range(self._months):
            result += f'Month #{mo+1}: \n'
            for d in range(self._days):
                result += f'Day #{d+1}: {self._calendar[mo][d]}\n' 
        return result
