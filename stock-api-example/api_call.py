import os

from dotenv import load_dotenv

from src.main.client import Client

load_dotenv()

API_KEY = os.getenv("API_TOKEN")

client = Client(API_KEY, "TSLA")

print(client.get_data())
