import requests

print(requests.get("http://0.0.0.0:8000/").text)

# Api Settings
# url = "http://0.0.0.0:8000/houses/"
# headers = {"Content-Type": "application/json"}

# post_data = {
#     "bedrooms": 4,
#     "bathrooms": 2.0,
#     "floors": 2.0,
#     "zipcode": 22769,
#     "last_change": 2023,
# }


# print(requests.post(url=url, json=post_data).json())
