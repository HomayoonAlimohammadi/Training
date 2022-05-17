from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import Any, List


class AlphabeticOrderIterator(Iterator):

    _position: int = None

    reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):

        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        
        except IndexError: 
            raise StopIteration()

        return value
        

class WordsCollection(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticOrderIterator:
        return AlphabeticOrderIterator(self._collection, False)

    def get_reverse_iterator(self) -> AlphabeticOrderIterator:
        return AlphabeticOrderIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


if __name__ == '__main__':

    collection = WordsCollection()
    collection.add_item('First Item')
    collection.add_item('Second Item')
    collection.add_item('Third Item')

    print('Straight traversal: ')
    for item in collection:
        print(item)
    print()

    print('Reverse Traversal: ')
    for item in collection.get_reverse_iterator():
        print(item)