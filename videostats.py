import requests
import json

API_KEY = 'AIzaSyDF6eYlz9yfpFnYRsux6McFKwwI3HWKNfc'


def get_channel_playlist(CANNEL_HANDLE):
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
    print("this will run in this only")
    get_channel_playlist("MrBeast")
else:
    print("running form somewhere else")
        