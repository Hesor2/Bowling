from bowling import calc_points
from api_handler import get_points, post_results
url = "http://13.74.31.101/api/points"
points, token = get_points(url)
print("Request has been sent to " + url)
print("Response contained following values:")
print("Points:", points)
print("Token", token)
results = calc_points(points)
print("Point sums calculated:", results)
status, success = post_results(url,results,token)
print("Status code:", status)
print("Succes:", success)