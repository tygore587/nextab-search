from dataclasses import dataclass
import json
import os
from typing import Sequence

from urllib.parse import urlencode
from urllib.request import urlopen

@dataclass
class Video:
    url: str
    name: str

playlistIdToCache = "UUHgGsiH1eoKXq90vrnnuWzg"

def _download_videos(api_key: str, playlist_id: str) -> Sequence[Video]:
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    
    query_params = {
        'part': 'snippet',
        'maxResults': 50,
        'playlistId': playlist_id,
        'key': api_key,
    }
    
    params_s = urlencode(query_params)
    
    response = urlopen(f'{url}?{params_s}')
    
    
    
    videos = []
    
    additional_pages = True
    
    while additional_pages:
        break
        
    
    
    return videos

def main() -> int:
    api_key = os.environ["YOUTUBE_API_KEY"]
    
    videos = _download_videos(api_key=api_key, playlist_id=playlistIdToCache)
    
    with open("videos.json", 'w') as file:
        json.dump(videos, file, seperators={",", ":"})
    
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())