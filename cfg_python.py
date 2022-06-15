from configparser import ConfigParser 


config = ConfigParser()
config.read('config.cfg')
key1 = config.get('section_1', 'key_1')
print(key1)
key2 = config['section_2']['key_2']
print(key2)

config.add_section('section_3')

# config.set(section, key, value)
config.set('section_3', 'key_3', 'value_3')

with open('config.cfg', 'w') as f:
    config.write(f)