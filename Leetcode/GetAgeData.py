import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
print(len(r.json()['data']))

data_dict = {}

data = r.json()['data']
while '=' in data:

    comma_index = data.index(',')
    equal_index = data.index('=')
    key = data[equal_index+1:comma_index]
    data = data[comma_index+1:]
    try:
        comma_index = data.index(',')
        
    except:
        comma_index = len(data)

    equal_index = data.index('=')
    age = data[equal_index+1:comma_index]
    data = data[comma_index+1:]

    data_dict[key] = float(age)

df = pd.DataFrame(
        data_dict.values(), 
        data_dict.keys(),
        columns=['age']
    ) 
                
print(df['age'].apply(lambda x: x>=50).sum())