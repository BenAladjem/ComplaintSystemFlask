import requests
import json
from decouple import config


class WiseService:
    def __init__(self):
        self.token = config("WISE_KEY")
        self.headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        self.main_url = config("WISE_URL")
        self.profile_id = self._get_profile_id()


    def _get_profile_id(self):
        url = f"{self.main_url}/v1/profiles"
        resp = requests.get(url, headers=self.headers)
        data = resp.json()
        profile_id = [o["id"] for o in data if o["type"] == "personal"][0]
        return profile_id

    def create_quote(self, source_currency, target_courency, amount):
        url = f"{self.main_url}/v2/quotes"
        data = {
            "sourceCurrency": source_currency,
            "targetCurrency": target_courency,
            "targetAmount": amount,
            "profile": self.profile_id

        }
        resp = requests.post(url, json=data, headers=self.headers)
        return resp.json()['id']


if __name__ == "__main__":
    wise = WiseService()
    print(wise.profile_id)
    print(wise.create_quote("EUR", "EUR", 20))