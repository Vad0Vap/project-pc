import os
import json
from src.parser import YouTubeParser


def test_video_info_extraction():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    parser = YouTubeParser(url)
    data = parser.get_video_info()

    assert isinstance(data, dict)
    assert "title" in data
    assert "author" in data
    assert "views" in data
    assert "streams" in data


def test_json_save():
    sample_data = {"test": "value"}
    filename = "test_output.json"

    YouTubeParser.save_to_json(sample_data, filename)

    assert os.path.exists(filename)

    with open(filename, "r", encoding="utf-8") as f:
        saved_data = json.load(f)

    assert saved_data == sample_data

    os.remove(filename)
