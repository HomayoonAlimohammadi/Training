from enum import Enum, auto
from typing import List
from random import choice


class Employee(Enum):
    CEO = auto()
    MANAGER = auto()
    SALES = auto()
    ENGINEERING = auto()
    MARKETING = auto()
    SEO = auto()
    ACCOUNTING = auto()
    IT = auto()
    HR = auto()
    OTHER = auto()


def generate_random_team(size: int) -> List[Employee]:
    """Generate a random team with exactly one CEO"""

    if size <= 0:
        raise ValueError("Team size must be more than 0.")

    team_no_ceo = list(Employee)
    team_no_ceo.remove(Employee.CEO)

    team = [choice(team_no_ceo) for _ in range(size - 1)]
    team.append(Employee.CEO)

    return team


def fire_random_employee(team: List[Employee]) -> List[Employee]:
    """Remove a random employee from the list. Remove CEO last"""
    team_no_ceo = team.copy()
    team_no_ceo.remove(Employee.CEO)

    if len(team_no_ceo) > 1:
        team.remove(choice(team_no_ceo))
    else:
        team.remove(Employee.CEO)

    return team
