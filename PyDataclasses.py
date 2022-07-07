from dataclasses import dataclass, field, asdict, astuple
from typing import List


@dataclass(frozen=True, order=True, eq=True)  # slots = True for python >= 3.10
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    friends: List[str] = field(default_factory=list, hash=False)

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.age)


person1 = Person("homayoon", 22, ["nooshin", "matin"])
person2 = Person("nooshin", 21)
person3 = Person("mobin", 16)
person4 = Person("nooshin", 21)
data = {person2: "yep", person4: "no"}

p = Person("nooshin", 21)
print(data[p])
