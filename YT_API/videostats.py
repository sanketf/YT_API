import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")

CANNEL_HANDLE = "Tseries"

def get_channel_playlist():
    try:
         url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername={CANNEL_HANDLE}&key={API_KEY}"
         response = requests.get(url)
         data = response.json()
         channel_items = data["items"][0]
         channel_playlist = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

         return channel_playlist
    
    except requests.exceptions.RequestException as e:
         raise e
    
if __name__ =="__main__":
    print(get_channel_playlist())

