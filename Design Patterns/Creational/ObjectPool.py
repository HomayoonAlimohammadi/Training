class UsefulObject:

    def __init__(self):
        self.setting = 0

    def reset(self):
        self.setting = 0


class ObjectPool:

    def __init__(self, num_copies):
        '''
        Initialize UsefulObject Pool
        with desired number of copies.
        '''
        self.pool = [UsefulObject() for _ in range(num_copies)]

    def acquire(self):
        '''Acquire an instance of UsefulObject'''
        if len(self.pool) == 0:
            self.pool.append(UsefulObject())

        return self.pool.pop()

    def release(self, reusable):
        '''
        Reset an instance of UsefulObject
        and return in the UsefulObject Pool
        '''
        reusable.reset()
        self.pool.append(reusable)

    def getNumReady(self):
        '''
        Get the number of ready to use
        Instances of UsefulObject
        '''
        return len(self.pool)


USEFUL_OBJECT_POOL = ObjectPool(10)

instance_1 = USEFUL_OBJECT_POOL.acquire()
print(USEFUL_OBJECT_POOL.getNumReady())
USEFUL_OBJECT_POOL.release(instance_1)
print(USEFUL_OBJECT_POOL.getNumReady())


