import requests
import json

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAFEAXAEAAAAAhUqhoiVe3mhSime7QbA2wM4IDF8%3DJw78cHulsfKtfUIBubOuM06JoX8gCCU1XHGvo0aosWw9rfMklz"

def search_twitter(query, tweet_fields, bearer_token = BEARER_TOKEN):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    response = requests.request("GET", url, headers=headers)

    print(response.status_code)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()