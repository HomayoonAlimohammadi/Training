from __future__ import annotations 
import unittest 


class Flight:
    def __init__(self, **flight_data):
        self.f_id = flight_data[0]
        self.org = flight_data[1]
        self.dest = flight_data[2]
        self.take_off_time = flight_data[3] 
        self.arrival_time = flight_data[4]
        self.price = flight_data[5]
        self.place = flight_data[6]


class Road:
    def __init__(self, drive_data):
        self.r_id = drive_data[0]
        self.org = drive_data[1]
        self.dest = drive_data[2]
        self.dist = drive_data[3]
        self.speed_lim = drive_data[4] 

class Agency:
    def __init__(self):
        flights = []
        flight_orgs = set()
        roads = []
        roads_orgs = set()

    def add_flight(self, flight_data):
        flight = Flight(flight_data)
        self.flights.append(flight)

    def add_road(self, road_data):
        road = Road(road_data)
        self.roads.append(road)

    def read_data(self, f_name: str = 'transportation.txt'):
        '''Open and read transportation data from a given file'''

        with open(f_name, 'r') as data:
            line = data.readline()
            while line != '</flights>':
                flight_data = data.readline().split('#')
                self.add_flight(flight_data)


            line = data.readline()
            while line != '</roads>':
                road_data = data.readline().split('#')
                self.add_road(road_data)

    def service(self):
        '''Assign a transportation routine to the passenger'''

        req = input().split('#')
        org, dest, time, passengers = req
        p_idx = passengers.index('(')
        n_passengers, ages = int(passengers[:p_idx]), passengers[p_idx:-1]
        ages = [int(age) for age in ages.split(',')]

        

    def find_flight(self, org, time):
        pass 

    def find_road(self, org, time):
        pass

    def print_results(self, results):
        if not results:
            print('No results found!')
        else:
            total_price = 0
            for result in results:
                print(f'''  
                type: {result['type']}
                references: {result['ref']}
                route: {result['route']}
                duration: {result['duration']}
                price: {result['price']}
                ********************************************
                ''')
                total_price += result['price']
            print(total_price)
            

class AgencyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.f_name = 'transportation_test.txt'
        agency = Agency()
    
    def test_read_data(self):
        self.agency.read_data(self.f_name)
        true_flights = []
        true_roads = []
        with open(self.f_name, 'r') as data:
            line = data.readline()
            while line != '</flights>':
                line = data.readline().split('#')
                true_flights.append(line)


            line = data.readline()
            while line != '</roads>':
                line = data.readline().split('#')
                true_roads.append(line)

        self.assertEqual(self.agency.flights, true_flights)
        self.assertEqual(self.agency.roads, true_roads)

    def test_add_flight(self):
        pass 

    def test_add_road(self):
        pass 


if __name__ == '__main__':
    agency = Agency()
    agency.client()