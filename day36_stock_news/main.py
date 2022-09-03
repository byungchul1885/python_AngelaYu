import logging as l
l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', 
              level=l.INFO, datefmt='%I:%M:%S')

import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+18068355905"
VERIFIED_NUMBER = "+821026509593"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "Z4F1JQPFGH6YSRFZ"
NEWS_API_KEY = "2f10e64247d84a2183e0a1b7436c69de"
TWILIO_SID = "ACcd0671cae2979d25f5b1c4298f487176"
TWILIO_AUTH_TOKEN = "91fc9c294a82d9618fe2a8ad4adba409"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
l.debug(f"\n{response}");

l.debug(f"\n{response.json()}");

data = response.json()["Time Series (Daily)"]
l.info(f"\n{data}");

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, 
# but the positive difference is 20. 
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) \
    - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)


    ## STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#If difference percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    # print(three_articles)

    ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}.\n"
        f"Brief: {article['description']}" 
        for article 
        in three_articles]
    
    # print(formatted_articles)
    
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    #TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
