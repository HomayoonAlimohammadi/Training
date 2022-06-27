from typing import Callable, List
import pytest
from hypothesis import given
import hypothesis.strategies as st
from property_based_testing.office import (
    Employee,
    fire_random_employee,
    generate_random_team,
)


@st.composite
def team(
    draw: Callable[[st.SearchStrategy[int]], int],
    min_value: int = 1,
    max_value: int = 20,
):
    random_value = draw(st.integers(min_value=min_value, max_value=max_value))
    return generate_random_team(random_value)


@given(st.integers(max_value=0))
def test_negative_team_size(size: int):
    with pytest.raises(ValueError):
        generate_random_team(size)


@given(team())
def test_team_has_ceo(team: List[Employee]):
    assert Employee.CEO in team


@given(team())
def test_fire_random_employee(team: List[Employee]):
    original_team = team.copy()
    team = fire_random_employee(team)
    assert len(team) == len(original_team.copy()) - 1
