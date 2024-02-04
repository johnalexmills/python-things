import requests

from .configs import HOST


class Client:
    def __init__(self, token, stock) -> None:
        self.host = HOST
        self.token = token
        self.stock = stock
        self.url = "https://" + self.host + "/" + self.stock

    def build_headers(self):
        """
        test
        """
        headers = {
            "X-RapidAPI-Key": self.token,
            "X-RapidAPI-Host": self.host,
        }

        return headers

    def get_data(self):
        headers = self.build_headers()
        print(headers)
        print(self.url)
        resp = requests.get(self.url, headers=headers)

        return resp.json()


if __name__ == "__main__":
    print("test from client")
