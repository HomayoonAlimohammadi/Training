from __future__ import annotations
from typing import Any, List


class Folder:
    def __init__(
        self, name: str, parent: Folder = None, sub_dirs: List[str, Folder] = None
    ) -> None:
        self.name = name
        self.parent = parent
        self._sub_dirs = sub_dirs if sub_dirs else []

    @property
    def sub_dir(self) -> List[str, Folder]:
        return sorted(self._sub_dirs)

    def add_sub_dir(self, sub_dir: str | Folder) -> None:
        self._sub_dirs.append(sub_dir)

    def __str__(self) -> str:
        result = f"{self.name}\n"
        for sub in self.sub_dirs:
            result += f"\t{sub}\n"
        return result

    def __repr__(self) -> str:
        return f"{self.name}"

    def __lt__(self, other: str | Folder):
        if isinstance(other, Folder):
            return self.name < other.name
        return self.name < other

    def __le__(self, other: str | Folder):
        if isinstance(other, Folder):
            return self.name <= other.name
        return self.name <= other

    def __gt__(self, other: str | Folder):
        if isinstance(other, Folder):
            return self.name > other.name
        return self.name > other

    def __ge__(self, other: str | Folder):
        if isinstance(other, Folder):
            return self.name >= other.name
        return self.name >= other

    def __eq__(self, other: str | Folder):
        if isinstance(other, Folder):
            return self.name == other.name
        return self.name == other

    def __ne__(self, other: str | Folder):
        if isinstance(other, Folder):
            return self.name != other.name
        return self.name != other


def path_parser(path: str) -> str:
    parent_dir = None
    directory = Folder()
    end_of_file = False
    while not end_of_file:
        slash_idx = path.find("\\")
        if slash_idx == -1:
            end_of_file = True
        if end_of_file:
            sub_dir_name = path
        else:
            sub_dir_name = path[:slash_idx]
        if "." not in sub_dir_name:
            sub_dir = Folder(name=sub_dir_name, parent=parent_dir)
