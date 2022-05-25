from __future__ import annotations
from typing import List, Optional
from random import sample, seed
import logging


FORMAT = '%(message)s'
logging.basicConfig(filename='heap.log', filemode='w',
                    format=FORMAT, level=logging.DEBUG)

### Not used in the implementation of Heap structure.
class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> None:
        return f'Node{{val: {self.val}, left: {self.left}, right: {self.right}}}'

    def __repr__(self) -> None:
        return f'{self.val}'


class Heap:

    def __init__(self, values: Optional[List[int]] = None, strategy: str = 'min') -> None:
        '''
        Initialize the Heap structure.
        values can be given to heapify a list.
        strategy: 'max' or 'min' determines the type of Heap structure.
        '''
        self._available_strategies = ['min', 'max']
        if strategy not in self._available_strategies:
            logging.error('ValueError: Invalid value for `strategy`.')
            raise ValueError('Invalid value for `strategy`.')

        logging.debug(f'Initializing Heap structure...')
        self.strategy = strategy
        logging.debug(f'{self.strategy=}')
        self.values = []
        if values:
            for value in values:
                self.insert(value)
        logging.debug(f'{self.values=}')

    def insert(self, value: int) -> None:
        '''
        Insert values to the Heap Structure.
        '''
        logging.debug(f'Inserting {value}...')
        if self.strategy == 'min':

            self.values.append(value)
            idx = len(self.values) - 1
            parent_idx = (idx - 1) // 2 

            while parent_idx >= 0:
                if self.values[idx] < self.values[parent_idx]:
                    self.values[idx], self.values[parent_idx] = \
                        self.values[parent_idx], self.values[idx]
                    logging.debug(f'swapped {self.values[idx]}, {self.values[parent_idx]}')
                    idx = parent_idx
                    parent_idx = (idx - 1) // 2 
                else:
                    break

        elif self.strategy == 'max':
            # logging.error(f'Not Implemented Error for {self.strategy=}')
            # raise NotImplementedError

            self.values.append(value)
            idx = len(self.values) - 1
            parent_idx = (idx - 1) // 2 

            while parent_idx >= 0:
                if self.values[idx] > self.values[parent_idx]:
                    self.values[idx], self.values[parent_idx] = \
                        self.values[parent_idx], self.values[idx]
                    logging.debug(f'swapped {self.values[idx]}, {self.values[parent_idx]}')
                    idx = parent_idx
                    parent_idx = (idx - 1) // 2 
                else:
                    break
        
        logging.debug(f'Inserted {value=}.')
        logging.debug(f'{self.values=}')
        logging.debug('')

    def remove_root(self) -> int:
        '''
        Removing and returnning the root node in the heap
        '''
        logging.debug('removing root node...')
        root = self.values[0]
        logging.debug(f'{root=}')
        self.values[0], self.values[-1] = self.values[-1], self.values[0]
        self.values.pop()

        if self.strategy == 'min':
            idx = 0
            # while there is at least a left child
            while 2 * idx + 1 < len(self.values):
                left_child_idx = 2 * idx + 1
                right_child_idx = None
                if 2 * idx + 2 < len(self.values):
                    right_child_idx = 2 * idx + 2

                logging.debug(f'{self.values=}')
                logging.debug(f'{idx=}: {self.values[idx]}')
                logging.debug(f'{left_child_idx=}: {self.values[left_child_idx]}')
                logging.debug(f'{right_child_idx=}: {self.values[right_child_idx]}')

                swap_idx = None
                if right_child_idx:
                    if self.values[right_child_idx] < self.values[left_child_idx]:
                        swap_idx = right_child_idx
                    else:
                        swap_idx = left_child_idx

                elif left_child_idx:
                    swap_idx = left_child_idx

                logging.debug(f'{swap_idx=}')
                logging.debug('')

                if swap_idx:
                    if self.values[idx] > self.values[swap_idx]:
                        self.values[idx], self.values[swap_idx] = \
                            self.values[swap_idx], self.values[idx]
                        idx = swap_idx
                        continue
                        
                logging.debug(f'not swapped, {self.values[idx]=}, {self.values[swap_idx]=}')
                
                break

        elif self.strategy == 'max':
            # logging.error(f'Not Implemented Error for {self.strategy=}')
            # raise NotImplementedError
            idx = 0
            # while there is at least a left child
            while 2 * idx + 1 < len(self.values):
                left_child_idx = 2 * idx + 1
                right_child_idx = None
                if 2 * idx + 2 < len(self.values):
                    right_child_idx = 2 * idx + 2

                logging.debug(f'{self.values=}')
                logging.debug(f'{idx=}: {self.values[idx]}')
                logging.debug(f'{left_child_idx=}: {self.values[left_child_idx]}')
                logging.debug(f'{right_child_idx=}: {self.values[right_child_idx]}')

                swap_idx = None
                if right_child_idx:
                    if self.values[right_child_idx] > self.values[left_child_idx]:
                        swap_idx = right_child_idx
                    else:
                        swap_idx = left_child_idx

                elif left_child_idx:
                    swap_idx = left_child_idx

                logging.debug(f'{swap_idx=}')
                logging.debug('')

                if swap_idx:
                    if self.values[idx] < self.values[swap_idx]:
                        self.values[idx], self.values[swap_idx] = \
                            self.values[swap_idx], self.values[idx]
                        idx = swap_idx
                        continue
                        
                logging.debug(f'not swapped, {self.values[idx]=}, {self.values[swap_idx]=}')
                
                break


        logging.debug(f'Returning {root=}...')
        logging.debug('')
        return root

    def __str__(self) -> None:
        return f'Heap: {self.values}'

    def __repr__(self) -> None:
        return str(self.values)
    

seed(0)
values = sample(range(1, 100), 7)
print(f'{values=}')
heap = Heap(values, strategy='min')
print(heap)
heap.insert(2)
print(heap)
print()
print(heap.remove_root())
print(heap)       
print()
heap = Heap(values, strategy='max')
print(heap)
heap.insert(2)
print(heap)
print()
print(heap.remove_root())
print(heap)  