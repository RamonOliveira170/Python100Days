import requests
from datetime import datetime
#https://pixe.la/v1/users/cristianoromaldo/graphs/graph1.html
USERNAME = "cristianoromaldo"
TOKEN = "12345678"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": "12345678",
    "username": "cristianoromaldo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.35",
    #"quantity": input("how many kilometers did you cycle today? ")
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

''' UPDATE A PIXEL
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.85"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)'''

''' DELETE A PIXEL
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)'''
