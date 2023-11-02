from dataclasses import dataclass
import dataclasses
import json
import os
from typing import Any, List, Sequence
from unittest import result

from urllib.parse import urlencode
from urllib.request import urlopen


@dataclass
class Video:
    url: str
    title: str


playlistIdToCache = "UUHgGsiH1eoKXq90vrnnuWzg"


def _download_videos(api_key: str, playlist_id: str) -> Sequence[Video]:
    url = "https://www.googleapis.com/youtube/v3/playlistItems"

    query_params = {
        "part": "snippet",
        "maxResults": 50,
        "playlistId": playlist_id,
        "key": api_key,
    }

    videos: Sequence[Video] = []

    additional_pages = True

    while additional_pages:
        params_s = urlencode(query_params)

        response = urlopen(f"{url}?{params_s}")

        print(". ", end="")

        responseData = json.load(response)

        videos.extend(
            _transform_video(new_video) for new_video in responseData["items"]
        )

        token = responseData.get("nextPageToken")

        if token:
            query_params["pageToken"] = token
        else:
            additional_pages = False

    print()

    return videos


def _transform_video(video: dict[str, Any]) -> Video:
    video_id = video["snippet"]["resourceId"]["videoId"]
    title = video["snippet"]["title"]

    return Video(title=title, url=f"https://youtu.be/{video_id}")


def main() -> int:
    api_key = os.environ["YOUTUBE_API_KEY"]

    print("Downloading youtube data.")
    
    videos = _download_videos(api_key=api_key, playlist_id=playlistIdToCache)

    print("Saving to file.")

    with open("videos.json", "w") as file:
        video_dicts = [dataclasses.asdict(video) for video in videos]

        json.dump(video_dicts, file, ensure_ascii=False)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
