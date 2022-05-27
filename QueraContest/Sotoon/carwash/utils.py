'''
Utility module.
'''

from typing import Tuple, List, Union


class ReservationTicket:

    def __init__(self, time: Union[str, Tuple[int, int]], car: str, services: List[str], user_id: Union[str, None]):
        self.time = time
        self.car = car
        self.services = services
        self.user_id = user_id

    def __str__(self):
        return f'ReservationTicket: {self.time}, {self.car}, {self.services}, {self.user_id}'
