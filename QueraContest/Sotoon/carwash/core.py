'''
Main part of the carwash package.\n
The `client` will send and receive messages from `CarWash` object(s).
'''

from __future__ import annotations
from carwash import CarWash
from typing import List, Callable
from utils import ReservationTicket


def reserve(args: str, carwash) -> bool:
    '''Reserve command implementation'''
    print(args)
    time = args[0]
    args = args[1:]
    if time != 'earliest':
        day, hour_min = time, args[0]
        hour, minute = hour_min.split(':')
        hour, minute = int(hour), int(minute)
        time = (hour, minute)
        args = args[1:]
    
    car = args[0]
    args = args[1:]

    services = args[0]
    services = services.split('+')
    args = args[1:]

    user_id = None
    if args:
        user_id = args[0]
        _, user_id = user_id.split('#')

    print(time, car, services, user_id)
    ticket = ReservationTicket(time, car, services, user_id)
    res = carwash.reserve(ticket)
    print(res)
    return True

def list_vip_members(args, carwash) -> True:
    '''List VIP members.'''
    empty = True
    for id, n_usage in carwash._users_record:
        if n_usage > 4:
            print(f'User #{id}')
            empty = False
    if empty:
        print('No VIP members at the moment. Become the first one!')
    return True

def exit(*args, **kwargs):
    print('Come back any time!')
    return False

def listener(line: str, carwash: CarWash) -> None:
    commands: dict[str, Callable[[str, CarWash], str]] = {
        'reserve': reserve,
        'vip-list': list_vip_members,
        'exit': exit,
    }
    parts = line.split()
    if parts[0] not in commands:
        print('Invalid command.')
    else:
        ans = commands[parts[0]](parts[1:], carwash)
    return ans

def main() -> None:
    carwash = CarWash()
    alive = True   
    while alive: 
        INPUT = input()
        alive = listener(INPUT, carwash)

if __name__ == '__main__':
    main()