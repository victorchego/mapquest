# Victor Chang

import MapQuestOutput
import MapQuestAPI

APPKEY = "NULLFORSECURITYREASONS"

def handle_commands() -> None:
    ''' Execute the program, take the inputs and outputs, and generate
    a formatted wall of text with the corresponding information '''
    
    dest_list = iterate_num()
    info_list = iterate_num()
    iterate_output(dest_list, info_list)    

def iterate_num() -> list:
    ''' Creates and returns a list of destinations or commands equal to the
    input value '''
    num = int(input())
    result = []
    for i in range(num):
        result.append(input())
    return result

def iterate_json(dest_list: list) -> ['json']:
    ''' Takes a list of destinations and returns a list of json objects '''
    result = []
    counter = 0
    for dest in range(len(dest_list)):
        if dest < len(dest_list) - 1:
            url = MapQuestAPI.build_search_url(dest_list[dest], dest_list[dest+1])
            counter = 0
        elif dest == len(dest_list) - 1:
            url = MapQuestAPI.build_search_url(dest_list[dest], dest_list[dest])
            counter = 1
        result.append(MapQuestAPI.get_result(url))
    return result            

def iterate_output(dest_list : list, info_list: list) -> list:
    ''' Generates and prints all the requested information based on the inputs
    and outputs '''
    print()
    json_list = iterate_json(dest_list)
    for info in range(len(info_list)):
        if info_list[info] == 'TOTALDISTANCE':
            dest_class = MapQuestOutput.Distance(json_list)
            dest_class.generate()
            print()
        elif info_list[info] == 'TOTALTIME':
            dest_class = MapQuestOutput.Time(json_list)
            dest_class.generate()
            print()
        elif info_list[info] == 'LATLONG':
            dest_class = MapQuestOutput.Coordinates(json_list)
            dest_class.generate()
            print()
        elif info_list[info] == 'STEPS':
            dest_class = MapQuestOutput.Steps(json_list)
            dest_class.generate()
            print()
    print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
 

if __name__ == "__main__":
    handle_commands()
