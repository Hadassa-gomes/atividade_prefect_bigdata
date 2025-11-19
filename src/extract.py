import requests

class Extract:
    def extract_data(self, country: str):
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
