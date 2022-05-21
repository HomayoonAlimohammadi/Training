import logging
from random import sample


FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'

logging.basicConfig(filename='test.log', filemode='w',
                    format=FORMAT, level=logging.DEBUG)

sample_nums = sample(range(-50,50), 20)
results = []
sample_nums.insert(10, 0)
for num in sample_nums:
    index = sample_nums.index(num)
    try:
        result = num / sample_nums[index-1]
        results.append(result)
    except ZeroDivisionError as e:
        logging.exception()
    except IndexError as e:
        logging.exception()






