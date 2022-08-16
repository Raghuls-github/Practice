import os
import requests
import json

bearer_token = os.environ.get('BEARER_TOKEN')
class Twitter(object):
    def search_twitter(query, tweet_fields, bearer_token=BEARER_TOKEN):
        header = {"Authorization": "Bearer {}".format(bearer_token)}
        url = "".format(
            query, tweet_fields
            )

        response = requests.request("GET", url, headers=header)
        print(response.status_code)

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
            return response.json()


query = input("Enter the keyword to search")
tweet.fields = "text, author_id, created_at"
json_response = search_twitter(query=query, tweet_fields=tweet_fields, bearer_token=BEARER_TOKEN)
print(json.dumps(json_response, indent=4, sort_keys=True))
