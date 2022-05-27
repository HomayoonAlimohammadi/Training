'''
carwash module containing the CarWash class.
'''

from __future__ import annotations
from typing import List
from calendar import Calendar
from utils import ReservationTicket


class CarWash:
    '''
    Main Car Wash class.
    '''

    def __init__(self) -> None:
        '''Initialize Car Wash with clean calendar and 0 users.'''
        self._calendar: Calendar = Calendar()
        self._users_record: dict[str] = {}
        self._services: dict[str, int]
        self._setup_services()
        self._cars: List[str]
        self._setup_cars()
        self._car_services: dict[str, dict[str, int]]
        self._setup_car_services()

    def _setup_cars(self) -> None:
        '''
        Set up cars with available services.\n
        '''
        cars = ['sedan', 'suv', 'hatchback']
        self._cars = cars
    
    def _setup_services(self) -> None:
        '''
        Set up services for the Car Wash.\n
        Base services would be: \n
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

    def _setup_car_services(self) -> None:
        '''
        Set up car services for the Car Wash.\n
        Including: `sedan`, `hatchback`, `suv`.\n
        Services are defined by the `._services` attribute.\n
        `car_services` would be like:\n
        {
            'suv': {
                'rooshooyi': 40,
                ...
            },
            ...
        }
        '''
        car_services = {
            'suv': {
                'rooshooyi': 40,
                'sefrshooyi': 100,
                'nezafat': 20
            },
            'hatchback': {
                'rooshooyi': 30,
                'sefrshooyi': 70,
                'nezafat': 10
            },
            'sedan': {
                'rooshooyi': 30,
                'sefrshooyi': 80,
                'nezafat': 15
            }
        }
        self._car_services = car_services

    def reserve(self, ticket: ReservationTicket) -> bool:
        '''Reserve time according to the ticket.'''

        total_time = 0
        for service in ticket.services:
            total_time += self._services[service]

        if ticket.time == 'earliest':
            res = self._calendar.fill_earliest(total_time)
        
        else:
            res = self._calendar.fill_specific(total_time, ticket.time)

        if not res['status']:
            return 'Reservation Failed.'
        
        return self.success(ticket, res)

    def success(self, ticket: ReservationTicket, res: dict) -> str:
        '''Success quote for reservation'''
        result = f"Reserved {res['time']}\n"
        result += f"Line: {res['line']}\n"
        result += f"Car Type: {res['car']}\n"
        result += f"User: {res['user']}\n"
        for service, price in zip(res['services'], res['prices']):
            result += f'- {service}: {price}'
        return result





        
