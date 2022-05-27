from __future__ import annotations
from typing import List
from calendar import Calendar


class CashWash:
    '''
    Main Car Wash class.
    '''

    def __init__(self) -> None:
        '''Initialize Car Wash with clean calender and 0 users.'''
        self._calender: Calendar = Calendar()
        self._user_list: dict[str] = {}
        self._services: dict[str, int]
        self._setup_services()
        self._cars: dict[str, dict[str, int]]
        self._setup_car_services()
    
    def _setup_services(self) -> None:
        '''
        Set up services for the Car Wash.
        Base services would be: 
        {
            'rooshooyi': 15,
            'sefrshooyi': 60,
            'nezafat': 20
        }
        '''
        services = {
            'rooshooyi': 15,
            'sefrshooyi': 60,
            'nezafat': 20
        }
        self._services = services

    def _setup_car_services(self) -> dict[str, dict[str, int]]:
        '''
        Set up car services for the Car Wash.
        Including: `sedan`, `hatchback`, `suv`.
        Services are defined by the `._services` attribute.
        Output format would be like: \n
        {
            'suv': {
                'rooshooyi': 40,
                ...
            },
            ...
        }
        '''
        for car in self._cars:
            for 