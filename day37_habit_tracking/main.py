import requests
from datetime import datetime

USERNAME = "bccho"
TOKEN = "2kakzDkk8!2@4sak"
GRAPH_ID = "bcgraph01"


# today = datetime.now()
# print(today)
# print(today.strftime("%Y%m%d"))


## POST : 사용자 만들기 --> https://pixe.la/@bccho
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(
#     url=pixela_endpoint, 
#     json=user_params)
# print(response.text)


## POST : 그래프 만들기
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
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
# response = requests.post(
#     url=graph_endpoint, 
#     json=graph_config, 
#     headers=headers)
# print(response.text)


## POST : 데이타 등록
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}
# response = requests.post(
#     url=pixel_creation_endpoint, 
#     json=pixel_data, 
#     headers=headers)
# print(response.text)


## PUT : 데이타 수정
update_endpoint = \
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5"
}
## PUT
# response = requests.put(
#     url=update_endpoint, 
#     json=new_pixel_data, 
#     headers=headers)
# print(response.text)


## DELETE : 데이타 삭제
delete_endpoint = \
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)