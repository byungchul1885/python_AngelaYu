#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import logging as l
l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', 
              level=l.INFO, datefmt='%I:%M:%S')

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
l.info(f"api_key: {api_key}")

weather_params = {
    "lat": "37.566536",
    "lon": "126.977966",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

l.info(f"weather_slice:\n{weather_slice}")

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    l.info(f"condition_code:\n{condition_code}")
    
    if int(condition_code) < 700:
        will_rain = True

# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}

#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Remember to bring an ☔️",
#         from_="YOUR TWILIO VIRTUAL NUMBER",
#         to="YOUR TWILIO VERIFIED REAL NUMBER"
#     )
#     print(message.status)


# Find your Account SID and Auth Token at twilio.com/console
# and set the e1nvironment variables. See http://twil.io/secure

#Twilio
account_sid = "ACcd0671cae2979d25f5b1c4298f487176"
#귀찮아서 직접 사용
auth_token = "91fc9c294a82d9618fe2a8ad4adba409" #os.environ.get("AUTH_TOKEN")

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="비가 올거에요. 우산을 챙기세요",
        from_='+18068355905',
        to='+821026509593')
    
    # message = client.messages \
    #             .create(
    #                 body="비가 올거에요. 우산을 챙기세요",
    #                 from_='+18068355905',
    #                 to='+821042713258'
    #             )