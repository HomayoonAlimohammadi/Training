from __future__ import annotations
from typing import List, Tuple


class Folder:
    def __init__(
        self, name: str, parent: Folder = None, sub_dirs: List[str, Folder] = None
    ) -> None:
        self.name = name
        self.parent = parent
        self._sub_dirs = sub_dirs if sub_dirs else []

    @property
    def sub_dirs(self) -> List[str, Folder]:
        return self._sub_dirs

    @sub_dirs.setter
    def sub_dirs(self, value: List[str, Folder]):
        self._sub_dirs = value

    def add_sub_dir(self, sub_dir: str | Folder) -> None:
        self._sub_dirs.append(sub_dir)

    def to_path_string(self) -> str:
        def dfs(dir: Folder | str, n_tabs: int = 0, path: str = "") -> str:
            if isinstance(dir, str):
                path += "\n" + n_tabs * "\t" + dir
                return path
            path += "\n" + n_tabs * "\t" + dir.name
            for sub_dir in dir.sub_dirs:
                path = dfs(sub_dir, n_tabs + 1, path)
            return path

        path = dfs(self)
        return path[1:]  # subtract first \n

    def __str__(self) -> str:
        result = f"{self.name}/\n"
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


def path_parser(path: str) -> Folder | str:

    slash_idx = path.find("\n")
    if slash_idx == -1:
        if "." in path:
            return path
        return Folder(path)
    else:
        root_name = path[:slash_idx]

    path = path[slash_idx:]
    root = Folder(root_name)

    def parse_sub_dirs(root: Folder, child_tabs: int, path: str) -> Tuple[Folder, str]:
        while path[0] == "\n":
            org_path = path
            path = path[1:]  # remove \n
            t_count = 0
            while path[t_count] == "\t":
                t_count += 1  # count # of \t

            path = path[t_count:]  # trim \t(s)
            if t_count == child_tabs:  # next is child
                slash_idx = path.find("\n")
                sub_dir = path[:slash_idx]
                path = path[slash_idx:]
                if "." not in sub_dir:
                    sub_dir = Folder(sub_dir)
                    # process sub_dirs and path
                    sub_dir, path = parse_sub_dirs(sub_dir, child_tabs + 1, path)

                root.sub_dirs += [sub_dir]
            elif t_count < child_tabs:
                return root, org_path
        return root, path

    root, _ = parse_sub_dirs(root, 1, path)
    return root


def main():
    root = Folder("dir")
    subdir1 = Folder("subdir1")
    subdir2 = Folder("subdir2")
    file1 = "file1.txt"
    subdir3 = Folder("subdir3")
    file2 = "file2.txt"

    subdir1.add_sub_dir(file1)
    subdir3.add_sub_dir(file2)
    subdir2.add_sub_dir(subdir3)
    root.add_sub_dir(subdir1)
    root.add_sub_dir(subdir2)
    root.add_sub_dir(subdir3)

    path = "dir\n\tsubdir1\n\t\tfile1.txt\n\tsubdir2\n\t\tsubdir3\n\t\t\tfile2.txt"

    root = path_parser(path)
    path = root.to_path_string()
    print(path)


if __name__ == "__main__":
    main()
