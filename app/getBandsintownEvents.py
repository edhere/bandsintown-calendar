from __future__ import print_function

import json
import requests
print('Loading function')


def lambda_handler(event, context):
    if not 'ids' in event.keys():
        raise LambdaException(json.dumps(event))
    ids = event['ids']
    response = {}
    if isinstance(ids, list):
        for id in ids:
            r = requests.get(
                "http://api.bandsintown.com/artists/"+id+"/events.json?api_version=2.0&app_id=FACTION"
            )
            all_results = r.json()
            if 'range' in event.keys():
                filtered_results = filter_results(event['range']['start'], event['range']['end'], all_results)
            else:
                filtered_results = all_results
            response[id] = filtered_results
    return response

def filter_results(start, end, all_results):
    filtered_results = []
    if start and end:
        filtered_results = []
        for result in all_results:
            if result:
                filtered_results.append(result)
    return filtered_results

class LambdaException(Exception):
    pass
