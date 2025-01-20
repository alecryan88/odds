import requests
import os


class oddsAPIClient:
    def __init__(self) -> None:
        self.key = 'ca135c3f78c4b1ce431c3df13b765c4f'
        self.host = 'https://api.the-odds-api.com/v4/'
        self.default_params = {
            'apiKey': self.key
        }

    def make_request(self, endpoint, params={}):
        url = self.host + endpoint
        print(url)
        call_dict = self.default_params.copy()
        call_dict.update(params)
        r = requests.get(url=url, params=call_dict)
        response_json = r.json()
        return response_json
