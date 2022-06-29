from __future__ import annotations
from typing import Dict, List, Set


class Node:
    def __init__(
        self,
        val: str,
        children: Dict[str, Node] = None,
        is_end: bool = False,
        n_hits: int = 0,
    ) -> None:
        self.val = val
        self.children = {} if children is None else children
        self.is_end = is_end
        self.n_hits = n_hits

    def __str__(self) -> str:
        return f"""Node(val: {self.val},
        children: {self.children},
        is_end: {self.is_end})
        """

    def __repr__(self) -> str:
        return f"""Node(val: {self.val})
        """


class Trie:
    def __init__(self, root_val: str = "") -> None:
        self.root = Node(root_val)

    def add_string(self, string: str) -> None:

        current = self.root
        for char in string:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

        current.is_end = True
        current.n_hits += 1

    def __str__(self) -> str:
        return str(self.root)

    def search_prefix(self, prefix: str) -> List[str]:
        current = self.root
        for char in prefix:
            try:
                current = current.children[char]
            except KeyError:
                return []

        def dfs(node: Node, until_now: str, result: Set[str]) -> List[str]:

            if node.is_end:
                result.add((until_now, node.n_hits))

            for child in node.children.values():
                result.union(dfs(child, until_now + child.val, result))

            return result

        results = dfs(current, prefix, set())
        return sorted(list(results), key=lambda x: (-x[1], x[0]))


trie = Trie()
words = ["dog", "deer", "deal", "dig", "dog"]
for word in words:
    trie.add_string(word)

print(trie.search_prefix("d"))
