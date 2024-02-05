import requests
from config import config  # Assuming you have a config module with the necessary configurations
from utils.conn_helper import ConnHelper  # Assuming you have a conn_helper module with the get_error_message function

class CohereAIWrapper:
    def __init__(self, api_key):
        self.API_BASE_URL = config['url']['cohere']['base']
        self.COHERE_VERSION = config['url']['cohere']['version']
        self.API_KEY = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.API_KEY}',
            'Cohere-Version': self.COHERE_VERSION,
        }

    def generate_text(self, params):
        url = config['url']['cohere']['completions']
        try:
            response = requests.post(f'{self.API_BASE_URL}{url}', json=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise Exception(ConnHelper.get_error_message(error))

    def generate_chat_text(self, params):
        url = '/chat'
        try:
            response = requests.post(f'{self.API_BASE_URL}{url}', json=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise Exception(ConnHelper.get_error_message(error))

    def get_embeddings(self, params):
        url = config['url']['cohere']['embed']
        try:
            response = requests.post(f'{self.API_BASE_URL}{url}', json=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise Exception(ConnHelper.get_error_message(error))
