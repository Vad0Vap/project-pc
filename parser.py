from pytube import YouTube
import json


class YouTubeParser:
    def __init__(self, url: str):
        self.url = url
        self.video = YouTube(url)

    def get_video_info(self) -> dict:
        return {
            "title": self.video.title,
            "author": self.video.author,
            "views": self.video.views,
            "publish_date": str(self.video.publish_date),
            "length_seconds": self.video.length,
            "description": self.video.description[:300] + "..." if len(self.video.description) > 300 else self.video.description,
            "streams": self._get_streams(),
        }

    def _get_streams(self):
        return [
            {
                "resolution": stream.resolution,
                "type": stream.mime_type,
                "filesize": stream.filesize
            }
            for stream in self.video.streams.filter(progressive=True).order_by('resolution')
        ]

    @staticmethod
    def save_to_json(data: dict, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
