import json
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

def get_points(api_url):
    """sends a GET request to given url, and returns points(list of two-element lists of integers), token"""
    # make GET request
    with urlopen(api_url) as response:
        source = response.read()
    # deserialize response data to python object
    data = json.loads(source)
    points = data["points"]
    token = data["token"]
    # return values from python object
    return points, token

def post_results(api_url, results, token):
    """sends a POST request to given url with a json object containing given results as request body and token as a url parameter, returns http status code, success of point sum calculation"""
    # prepares url with token parameter
    query_string = urlencode({"token": token}) 
    url = "{}?{}".format(api_url,query_string)
    # prepare request object
    req = Request(url)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    # prepare and encode json data for body
    json_data = json.dumps({"points":results})
    json_bytes = json_data.encode("utf-8")
    # make request
    with urlopen(req, json_bytes) as response:
        source = response.read()
    # deserialize data into python object
    response_data = json.loads(source)
    success = response_data["success"]
    # return http status code and success json value
    return response.getcode(), success