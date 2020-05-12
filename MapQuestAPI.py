# Victor Chang
import json
import urllib.parse
import urllib.request

APPKEY = "NULLFORSECURITYREASONS"
BASE_URL = 'http://open.mapquestapi.com/directions/v2'

def build_search_url(from_dest: str, to_dest: str) -> str:
    '''  Takes two locations and builds and returns a URL that can
    be used to ask the MapQuest Data API for information about the
    directions matching the search request.'''
    query_parameters = [
        ('from', from_dest), ('to', to_dest)
    ]
    return BASE_URL + '/route?key=' +APPKEY + "&" + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> 'json':
    ''' Takes a URL and returns a Python object representing the parsed
    JSON response. '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()
