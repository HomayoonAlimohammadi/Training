class Node:

    def __init__(self, val, children=None):
        self.val = val
        self.ends = 0
        self.children = children or {}

    def __str__(self):
        return f'Node[val: {self.val}, ends: {self.ends}, children: {self.children}]'

    def __repr__(self):
        return f'{self.val}'


class Trie:

    def __init__(self):
        '''Initializes the Trie with the root being an empty string.'''
        self.root = Node('')

    def insert(self, word: str) -> None:
        '''Inserts a word to the Trie.'''
        
        curr = self.root
        for char in word:
            if char not in curr.children:
                node = Node(char)
                curr.children[char] = node

            curr = curr.children[char]
        curr.ends += 1


    def search(self, word: str, is_prefix: bool = False) -> bool:
        '''
        Search for a given word in the Trie, returns True if exists.
        Otherwise returns False.
        '''

        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True if (curr.ends or is_prefix) else False

    def startsWith(self, prefix: str) -> bool:
        '''
        Search to see if any word in the Trie starts with the given string.
        Returns True if exists and False otherwise.
        '''
        return self.search(word=prefix, is_prefix=True)


trie = Trie()
trie.insert('apple')
print(trie.search('apple'))
print(trie.search('app'))
print(trie.startsWith('app'))
trie.insert('app')
print(trie.search('app'))
