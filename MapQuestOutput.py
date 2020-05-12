# Victor Chang 

class Time():
    def __init__(self, json_list: list) -> None:
        ''' Takes all of the points in the maneuevers and adds each time
        interval to the total (route) time '''
        self._route_time = 0
        for json in json_list:
            point_list = json['route']['legs'][0]['maneuvers']
            for points in range(len(point_list)):
                self._route_time += point_list[points]['time'] #seconds
        
    def generate(self):
        ''' Prints the time for the route between two destinations '''
        print("Total Time: " + str(round(self._route_time/60)) + ' minutes')

class Distance():
    def __init__(self, json_list: list):
        ''' Takes all of the points in the maneuevers and adds each distance
         to the total (route) distance '''
        self._route_distance = 0
        for json in json_list:
            point_list = json['route']['legs'][0]['maneuvers']
            for points in range(len(point_list)):
                self._route_distance += point_list[points]['distance']
        
    def generate(self):
        ''' Returns the distance for the route between two destinations '''
        print("Total Distance: " + str(round(self._route_distance)) + ' miles')
        
class Steps():
    def __init__(self, json_list: list):
        ''' Takes all navigational directions and appends them to a list '''
        self._route_list = []
        for json in json_list[:-1]: #account for the extra "duplicate" destination
            point_list = json['route']['legs'][0]['maneuvers']
            for points in range(len(point_list)):
                self._route_list.append(point_list[points]['narrative'])
            
    def generate(self):
        ''' Prints the directions between the input destinations  '''
        print("DIRECTIONS")
        for point in self._route_list:
            print(point)

class Coordinates():
    def __init__(self, json_list: list):
        '''Pass on the list of json objects to its own attribute '''
        self._point_list = json_list
            
    def generate(self):
        ''' Prints the latitude and longitude with the cardinal directions
        of each location'''
        for point in self._point_list:           
            self._lat = point['route']['locations'][0]['latLng']['lat']
            self._long = point['route']['locations'][0]['latLng']['lng']
            if self._lat < 0:
                self._latdir = 'S'
                self._lat *= -1
            else:
                self._latdir = 'N'
            if self._long < 0:
                self._longdir = 'W'
                self._long *= -1
            else:
                self._longdir = 'E'
            print("{0:.2f}".format(self._lat) + self._latdir + ' ' + "{0:.2f}".format(self._long) \
                + self._longdir)
