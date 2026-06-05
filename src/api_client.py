import requests
import pandas as pd

class ApiClient:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def pull_data(self, endpoint: str) -> pd.DataFrame:
        """Retrieves data from mock api"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = (requests.get(url, timeout=10))
        response.raise_for_status()
        json_response = response.json()
        data_frame_response = pd.DataFrame(json_response)
        return data_frame_response




